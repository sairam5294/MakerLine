# Security — {{product}}

_Updated {{date}} · Baselines: OWASP Top 10:2025, ASVS 5 {{, MASVS v2 (mobile), LLM Top 10 (AI)}} · Standard: `.agents/skills/product-standards/references/security.md` · Privacy: `privacy.md`_

## 1. Threat model
- **Assets:** {{user accounts, personal data (list), payments, content, API keys, admin access}}
- **Actors:** anonymous visitor · signed-in user · group member/staff · admin · third-party services · a malicious user with a valid account · an attacker with a leaked client build
- **Entry points:** {{public web, app API, auth endpoints, webhooks, file uploads, admin UI, AI prompts}}
- **Top abuse cases:** {{3–5: e.g. read another user's rows by guessing ids; spam bookings; prompt injection via user content}} → each has a control below.

## 2. Controls (OWASP Top 10:2025)
| Risk | Control in this project | Where (file / service) | Verified by |
|---|---|---|---|
| A01 Broken access control | server-side authz on every endpoint; RLS on every table (`DATABASE.md` §3) | | RLS tests |
| A02 Security misconfiguration | headers (CSP, HSTS, X-Content-Type-Options, frame-ancestors); CORS allow-list; buckets private; no debug in prod | | header check in CI |
| A03 Supply chain | lockfile; Dependabot; audit in CI; actions pinned to SHAs; verify package names | | CI |
| A04 Cryptographic failures | TLS everywhere; auth provider hashes passwords; tokens in secure storage | | |
| A05 Injection | parameterized queries / ORM; schema validation on the server; output encoding | | tests |
| A06 Insecure design | rate limits on auth, OTP, search, AI, uploads; business limits ({{max items / spend}}) | | |
| A07 Authentication | {{provider}}; passkeys/OTP/magic link; MFA for admin; lockout/backoff | | |
| A08 Integrity | webhooks verified by signature; signed builds; least-privilege CI tokens | | |
| A09 Logging & alerting | auth, permission failures, admin and payment events logged without personal data; alerts on spikes | | |
| A10 Exceptional conditions | fail closed; every error path handled; no stack traces to users | | |

## 3. Secrets
- `.env*` ignored; `.env.example` committed with placeholders; gitleaks pre-commit + CI.
- Client bundles are public: only publishable/anon keys there; service keys server-only. Rotate anything ever exposed.
- Who holds what: {{owner's password manager; CI secrets list}}.

## 4. Auth and sessions
- Provider {{…}}; access token {{n}} min, refresh rotation; sign-out everywhere; password reset flow; admin MFA.
- Accessible authentication (WCAG 3.3.8): no CAPTCHA puzzles without an alternative; paste and password managers allowed.

## 5. Data protection and privacy
- Laws in scope: {{DPDP (India) / GDPR / PIPEDA / PHIPA / COPPA …}} from EVALUATION §11.
- Personal-data inventory: `DATABASE.md` §2 · Purpose and consent: {{…}} · Export and delete: {{function / screen}} · Retention: {{…}} · Processors: {{list}}.
- Children: {{not in scope / verifiable parental consent via …}}.

## 6. AI features (if any)
- Server-side calls only; prompt injection defences (user content never becomes instructions; tool permissions minimal); output labelled as AI; cost caps and rate limits; evals before launch (`AI_FEATURE_*.md`).

## 7. Mobile (if any)
- MASVS: secure storage, certificate pinning decision ({{yes/no, why}}), no secrets in the binary, obfuscation and debug off for release.

## 8. Incident basics
- Detect: {{error tracking, uptime monitor, provider alerts}} · Contact: {{owner email}} · First hour: rotate keys, revoke sessions, snapshot logs, tell affected users within {{n}} h if personal data is involved (`privacy.md`).

## 9. Expert review
- Required before launch if payments, children's data, health or finance data, or > 10k users (`ship-checklist/references/expert-review.md`). Status: {{…}}
