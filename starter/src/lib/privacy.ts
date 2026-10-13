/**
 * Privacy helpers shared by error tracking and analytics.
 * Rule (privacy standard): personal data never leaves the device in logs, crash reports or events.
 */

// Property names that usually hold personal data. Matched case-insensitively.
const PERSONAL_KEYS =
  /(e-?mail|phone|mobile|name|address|dob|birth|password|token|otp|aadhaar|pan|upi)/i;

// Values that look like an email or an Indian/international phone number.
const EMAIL = /[\w.+-]+@[\w-]+\.[\w.-]+/g;
const PHONE = /(\+?\d[\d\s-]{8,}\d)/g;

/** Replaces emails and phone numbers inside free text (e.g. an error message). */
export function scrubText(text: string): string {
  return text.replace(EMAIL, '[email]').replace(PHONE, '[phone]');
}

type Primitive = string | number | boolean | null;

/**
 * Keeps only safe analytics properties: drops personal-looking keys, scrubs strings,
 * and drops nested objects (they're where personal data hides).
 */
export function sanitizeProps(props: Record<string, unknown> = {}): Record<string, Primitive> {
  const clean: Record<string, Primitive> = {};
  for (const [key, value] of Object.entries(props)) {
    if (PERSONAL_KEYS.test(key)) continue;
    if (typeof value === 'string') clean[key] = scrubText(value).slice(0, 200);
    else if (typeof value === 'number' || typeof value === 'boolean' || value === null)
      clean[key] = value;
  }
  return clean;
}
