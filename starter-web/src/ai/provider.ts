import 'server-only';
import type { z } from 'zod';

/**
 * AI provider wrapper — every AI feature goes through here (ai.md standard):
 *  • server-only (the API key never reaches the browser)
 *  • timeout + one retry + typed fallback instead of a crash
 *  • output must match a Zod schema (structured output), otherwise it's rejected
 * Swap providers by writing another `ModelCall` — features don't change.
 */
export type ModelCall = (req: {
  system: string;
  user: string;
  maxTokens: number;
}) => Promise<string>;

export type AiResult<T> =
  | { ok: true; data: T }
  | { ok: false; reason: 'disabled' | 'timeout' | 'invalid_output' | 'error' };

/** Anthropic Messages API. Needs ANTHROPIC_API_KEY and AI_MODEL (pick the current model id from Anthropic's docs). */
export const anthropicCall: ModelCall = async ({ system, user, maxTokens }) => {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      'x-api-key': process.env.ANTHROPIC_API_KEY!,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify({
      model: process.env.AI_MODEL,
      max_tokens: maxTokens,
      system,
      messages: [{ role: 'user', content: user }],
    }),
    signal: AbortSignal.timeout(30_000), // never leave the user waiting forever
  });
  if (!res.ok) throw new Error(`AI provider HTTP ${res.status}`);
  const body = (await res.json()) as { content?: { type: string; text?: string }[] };
  return body.content?.find((c) => c.type === 'text')?.text ?? '';
};

export const aiEnabled = () => Boolean(process.env.ANTHROPIC_API_KEY && process.env.AI_MODEL);

/** Pull the first {...} JSON object out of a reply (models sometimes wrap it in prose/code fences). */
export function extractJson(text: string): unknown {
  const start = text.indexOf('{');
  const end = text.lastIndexOf('}');
  if (start < 0 || end <= start) throw new Error('no JSON object in reply');
  return JSON.parse(text.slice(start, end + 1));
}

/** Call the model, validate against `schema`, retry once on bad output, never throw. */
export async function generateStructured<T>(
  schema: z.ZodType<T>,
  req: { system: string; user: string; maxTokens?: number },
  call: ModelCall = anthropicCall,
): Promise<AiResult<T>> {
  if (call === anthropicCall && !aiEnabled()) return { ok: false, reason: 'disabled' };
  for (let attempt = 0; attempt < 2; attempt++) {
    let text: string;
    try {
      text = await call({ ...req, maxTokens: req.maxTokens ?? 800 });
    } catch (err) {
      if (err instanceof Error && err.name === 'TimeoutError')
        return { ok: false, reason: 'timeout' };
      if (attempt === 1) return { ok: false, reason: 'error' };
      continue; // provider hiccup → retry once
    }
    try {
      const parsed = schema.safeParse(extractJson(text));
      if (parsed.success) return { ok: true, data: parsed.data };
    } catch {
      // not JSON at all → counts as invalid output; retry once
    }
  }
  return { ok: false, reason: 'invalid_output' };
}
