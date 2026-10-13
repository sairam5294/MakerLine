import { describe, expect, it, vi } from 'vitest';
import { summariseFeedback, redact } from '@/ai/features/summariseFeedback';
import { extractJson, generateStructured, type ModelCall } from '@/ai/provider';
import { z } from 'zod';

const good = JSON.stringify({
  themes: [{ title: 'Crashes', count: 2, quote: 'crashes' }],
  sentiment: 'mixed',
});
const schema = z.object({ a: z.number() });

describe('generateStructured (AI safety net)', () => {
  it('returns validated data', async () => {
    const call: ModelCall = async () => 'Sure! ```json\n{"a": 1}\n```';
    expect(await generateStructured(schema, { system: 's', user: 'u' }, call)).toEqual({
      ok: true,
      data: { a: 1 },
    });
  });
  it('retries once when the output has the wrong shape', async () => {
    const call = vi
      .fn<ModelCall>()
      .mockResolvedValueOnce('{"a":"nope"}')
      .mockResolvedValueOnce('{"a":2}');
    expect(await generateStructured(schema, { system: 's', user: 'u' }, call)).toEqual({
      ok: true,
      data: { a: 2 },
    });
    expect(call).toHaveBeenCalledTimes(2);
  });
  it('gives a typed failure instead of crashing', async () => {
    const bad: ModelCall = async () => 'I cannot help';
    expect(await generateStructured(schema, { system: 's', user: 'u' }, bad)).toEqual({
      ok: false,
      reason: 'invalid_output',
    });
    const down: ModelCall = async () => {
      throw new Error('503');
    };
    expect(await generateStructured(schema, { system: 's', user: 'u' }, down)).toEqual({
      ok: false,
      reason: 'error',
    });
  });
  it('is disabled (no network call) without API key + model', async () => {
    expect(await generateStructured(schema, { system: 's', user: 'u' })).toEqual({
      ok: false,
      reason: 'disabled',
    });
  });
  it('extracts JSON wrapped in prose', () => {
    expect(extractJson('Here: {"x":1} done')).toEqual({ x: 1 });
  });
});

describe('summariseFeedback', () => {
  it('redacts personal data before it reaches the model', async () => {
    let sent = '';
    const call: ModelCall = async ({ user }) => ((sent = user), good);
    await summariseFeedback('u1', ['mail me at sai@example.com or +91 98765 43210'], call);
    expect(sent).not.toContain('sai@example.com');
    expect(sent).not.toContain('98765');
    expect(redact('a@b.co')).toBe('[email]');
  });
  it('handles empty input without calling the model', async () => {
    const call = vi.fn<ModelCall>();
    expect(await summariseFeedback('u2', ['  '], call)).toEqual({ ok: false, reason: 'empty' });
    expect(call).not.toHaveBeenCalled();
  });
  it('enforces the daily per-user quota (cost cap)', async () => {
    const call: ModelCall = async () => good;
    for (let i = 0; i < 20; i++) await summariseFeedback('heavy-user', ['x'], call);
    expect(await summariseFeedback('heavy-user', ['x'], call)).toEqual({
      ok: false,
      reason: 'quota',
    });
  });
});
