# Expert Review Brief (send to a security/legal professional)

What to send a professional reviewer before launch, and what to ask back — read by `ship-checklist` when payments, children's data, health/finance data or > 10k users are involved.

AI review is not enough when real money, children's data, sensitive data or scale are involved. Budget a few hours of a professional's time.

## Who

| Reviewer | When | Covers |
|---|---|---|
| Application-security reviewer | always | auth, payments, data access |
| Privacy lawyer | always (and/or the above) | DPDP/GDPR/COPPA, store rules, terms |
| Accessibility specialist (IAAP WAS or CPACC certified is a good signal) | when selling to businesses or government, launching in the EU/Ontario/US public sector, or serving disabled users as a core audience | a WCAG-EM audit and the ACR (VPAT) |

## Send them (generate from docs/product)

1. One-page product summary + audience (incl. children?) + markets
2. Data inventory: every personal-data field, purpose, storage location, retention, processors (Supabase, analytics, email, AI provider)
3. Architecture diagram + auth flow + payment flow
4. RLS policies / authorization rules + their tests
5. Latest quality-review security findings and fixes
6. Privacy policy, terms, consent screens (screenshots)
7. Specific questions (e.g. "Is our parental consent flow verifiable under DPDP?")

## Ask for

- Prioritised findings (Critical/High/Medium/Low)
- Required fixes before launch
- A short written sign-off

## Record

- Record the outcome in RELEASE.md and DECISIONS.md.
