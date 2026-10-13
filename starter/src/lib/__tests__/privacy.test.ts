import { sanitizeProps, scrubText } from '../privacy';

describe('scrubText', () => {
  it('removes emails and phone numbers from messages', () => {
    expect(scrubText('Failed for sai@example.com / +91 98765 43210')).toBe(
      'Failed for [email] / [phone]',
    );
  });
});

describe('sanitizeProps', () => {
  it('drops personal keys, nested objects and scrubs strings', () => {
    expect(
      sanitizeProps({
        lesson_id: 'l-12',
        minutes: 4,
        email: 'a@b.com',
        userName: 'Sai',
        note: 'call me on 9876543210',
        profile: { city: 'Hyderabad' },
      }),
    ).toEqual({ lesson_id: 'l-12', minutes: 4, note: 'call me on [phone]' });
  });
});
