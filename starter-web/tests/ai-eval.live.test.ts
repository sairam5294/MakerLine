/**
 * LIVE AI eval (costs a few cents): runs every case in evals/ai/*.cases.json against the real model.
 * Run with:  ANTHROPIC_API_KEY=… AI_MODEL=… npm run ai:eval
 * Skipped in normal `npm test`. Re-run after ANY prompt or model change; keep the pass rate ≥ 80%.
 */
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { describe, expect, it } from 'vitest';
import { PROMPT_VERSION, summariseFeedback } from '@/ai/features/summariseFeedback';

type Case = {
  id: string;
  comments: string[];
  expect: {
    minThemes?: number;
    mustMention?: string[];
    mustNotMention?: string[];
    sentiment?: string[];
  };
};
const cases: Case[] = JSON.parse(readFileSync('evals/ai/summarise-feedback.cases.json', 'utf8'));

describe.skipIf(!process.env.RUN_AI_EVALS)('AI eval: summarise-feedback', () => {
  it('meets the pass bar', { timeout: 300_000 }, async () => {
    const rows: string[] = [];
    let passed = 0;
    for (const c of cases) {
      const r = await summariseFeedback(`eval-${c.id}`, c.comments);
      const text = r.ok ? JSON.stringify(r.data).toLowerCase() : '';
      const problems: string[] = [];
      if (!r.ok) problems.push(`failed: ${r.reason}`);
      else {
        if ((c.expect.minThemes ?? 0) > r.data.themes.length) problems.push('too few themes');
        for (const w of c.expect.mustMention ?? [])
          if (!text.includes(w.toLowerCase())) problems.push(`missing "${w}"`);
        for (const w of c.expect.mustNotMention ?? [])
          if (text.includes(w.toLowerCase())) problems.push(`leaked "${w}"`);
        if (c.expect.sentiment && !c.expect.sentiment.includes(r.data.sentiment))
          problems.push(`sentiment ${r.data.sentiment}`);
      }
      if (problems.length === 0) passed++;
      rows.push(`| ${c.id} | ${problems.length ? '✖ ' + problems.join('; ') : '✔'} |`);
    }
    const rate = passed / cases.length;
    const report = `# AI eval — ${PROMPT_VERSION} — model ${process.env.AI_MODEL} — ${new Date().toISOString().slice(0, 10)}\n\nPass rate: ${Math.round(rate * 100)}%\n\n| Case | Result |\n|---|---|\n${rows.join('\n')}\n`;
    mkdirSync('evals/ai/results', { recursive: true });
    writeFileSync(`evals/ai/results/${PROMPT_VERSION}-${Date.now()}.md`, report);
    console.log(report);
    expect(rate).toBeGreaterThanOrEqual(0.8);
  });
});
