import { validateEmail } from '../signInSchema';

describe('validateEmail', () => {
  it.each([
    ['', 'errors.emailRequired'],
    ['   ', 'errors.emailRequired'],
    ['sai@', 'errors.emailInvalid'],
  ])('%j → %s', (input, message) => {
    expect(validateEmail(input)).toBe(message);
  });

  it('accepts a valid email with surrounding spaces', () => {
    expect(validateEmail('  sai@example.com ')).toBeUndefined();
  });
});
