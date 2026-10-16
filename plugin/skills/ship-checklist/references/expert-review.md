# Expert Review Brief (send to a security/legal professional)

AI review is not enough when real money, children's data, sensitive data or scale are involved. Budget a few hours of a professional's time.

**Who**: application-security reviewer (auth, payments, data access) and/or privacy lawyer (DPDP/GDPR/COPPA, store rules, terms), and — when selling to businesses or government, launching in the EU/Ontario/US public sector, or serving disabled users as a core audience — an accessibility specialist (IAAP WAS or CPACC certified is a good signal) for a WCAG-EM audit and the ACR (VPAT).

**Send them** (generate from docs/product):
1. One-page product summary + audience (incl. children?) + markets
2. Data inventory: every personal-data field, purpose, storage location, retention, processors (Supabase, analytics, email, AI provider)
3. Architecture diagram + auth flow + payment flow
4. RLS policies / authorization rules + their tests
5. Latest quality-review security findings and fixes
6. Privacy policy, terms, consent screens (screenshots)
7. Specific questions (e.g. "Is our parental consent flow verifiable under DPDP?")

**Ask for**: prioritised findings (Critical/High/Medium/Low), required fixes before launch, and a short written sign-off. Record in RELEASE.md and DECISIONS.md.
