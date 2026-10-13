import 'server-only';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import { z } from 'zod';
import { createRateLimiter } from '@/lib/rateLimit';
import { generateStructured, type AiResult, type ModelCall } from '../provider';

/**
 * Example AI feature: summarise user feedback into themes (e.g. for post-launch reviews).
 * Copy this pattern for new features: versioned prompt file + Zod schema + redaction + quota.
 * Eval set: evals/ai/summarise-feedback.cases.json (run: npm run ai:eval).
 */
export const PROMPT_VERSION = 'summarise-feedback.v1';
const system = readFileSync(join(process.cwd(), 'src/ai/prompts', `${PROMPT_VERSION}.md`), 'utf8');

export const feedbackSummarySchema = z.object({
  themes: z
    .array(
      z.object({
        title: z.string().min(2).max(80),
        count: z.number().int().min(1),
        quote: z.string().max(300),
      }),
    )
    .max(5),
  sentiment: z.enum(['positive', 'mixed', 'negative']),
});
export type FeedbackSummary = z.infer<typeof feedbackSummarySchema>;

/** Remove emails and phone numbers before anything is sent to an AI provider (privacy standard). */
export function redact(text: string): string {
  return text
    .replace(/[\w.+-]+@[\w-]+\.[\w.-]+/g, '[email]')
    .replace(/(\+?\d[\d\s-]{8,}\d)/g, '[phone]');
}

// Cost cap: 20 summaries per user per day.
const dailyQuota = createRateLimiter({ limit: 20, windowMs: 24 * 60 * 60 * 1000 });

export async function summariseFeedback(
  userId: string,
  comments: string[],
  call?: ModelCall,
): Promise<AiResult<FeedbackSummary> | { ok: false; reason: 'quota' | 'empty' }> {
  const clean = comments
    .map((c) => redact(c.trim()))
    .filter(Boolean)
    .slice(0, 200);
  if (clean.length === 0) return { ok: false, reason: 'empty' };
  if (!dailyQuota(userId).ok) return { ok: false, reason: 'quota' };

  const user =
    `Feedback (${clean.length} comments):\n` + clean.map((c, i) => `${i + 1}. ${c}`).join('\n');
  return generateStructured(feedbackSummarySchema, { system, user, maxTokens: 800 }, call);
}
