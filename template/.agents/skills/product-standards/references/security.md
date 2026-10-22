# Security Standard

Baselines: **OWASP Top 10:2025**, **OWASP ASVS 5** (web/API), **OWASP MASVS v2** (2.1.0, mobile; test with MASTG v2), **OWASP Top 10 for LLM Applications** (if the product uses AI). Security is designed in, not bolted on. *(Last verified 2026-10-20.)*

## 1. OWASP Top 10:2025 → what we do

| Risk | MUST controls |
|---|---|
| A01 Broken Access Control | Deny by default; check ownership/role on the server for every read and write; database row-level security (e.g. Supabase RLS) enabled on every table; test that user A can't access user B's data; no IDs that grant access just by guessing |
| A02 Security Misconfiguration | No debug/verbose errors in production; security headers (CSP, HSTS, X-Content-Type-Options, frame-ancestors); CORS allow-list, never `*` with credentials; storage buckets private by default |
| A03 Software Supply Chain Failures | Lockfiles committed; Dependabot/Renovate; `npm audit`/OSV in CI; verify package names (typosquatting, AI-hallucinated packages); minimal dependencies; pin GitHub Actions to SHAs |
| A04 Cryptographic Failures | HTTPS/TLS 1.2+ everywhere; never roll your own crypto; passwords hashed by the auth provider (argon2/bcrypt); encrypt sensitive data at rest; tokens in secure storage (Keychain/Keystore/`expo-secure-store`, httpOnly cookies on web) |
| A05 Injection | Parameterized queries/ORM only; validate input with schemas on the server; output-encode; never run user data as code or insert it as raw HTML (React's dangerouslySetInnerHTML); sanitize rich text |
| A06 Insecure Design | Threat-model each feature (who could abuse it, how); rate limits on auth, OTP, search, AI and any costly endpoint; business-logic limits (max items, max spend) |
| A07 Authentication Failures | Use a proven provider (Supabase Auth, Clerk, Firebase Auth, Auth0); passkeys/OTP/magic links; MFA for admin; short-lived access tokens + rotating refresh; lockout/backoff on repeated failures; secure password reset |
| A08 Software/Data Integrity Failures | Verify webhooks by signature; signed builds; CI with least-privilege tokens; no unsigned auto-updates; validate deserialized data |
| A09 Logging & Alerting Failures | Log auth events, permission failures, admin actions, payment events — without secrets or personal data; alerting on spikes (Sentry, provider alerts) |
| A10 Mishandling of Exceptional Conditions | Fail closed (errors deny access, never grant); catch and handle every error path; no stack traces to users; transactions roll back on failure |

## 2. Secrets

- **MUST** never commit secrets. `.env*` in `.gitignore`; `.env.example` with placeholders only. Run gitleaks (pre-commit + CI).
- Client apps (web bundles, mobile apps) are public: anything shipped to the client is NOT secret. Only publishable/anon keys on the client; service-role keys only on the server.
- Rotate any key that was ever exposed — deleting the commit is not enough.

## 3. API security

- Authenticate every non-public endpoint; authorize every object access.
- Validate request body, params and query against a schema; reject unknown fields.
- Rate limit per user and per IP; return generic auth errors ("Invalid email or password").
- Paginate lists; cap page size; never return more fields than the client needs (no password hashes, internal flags).
- File uploads: check type by content, cap size, store outside web root / in private buckets, serve via signed URLs, scan if user-shared.

## 4. Mobile (MASVS v2)

- Store tokens only in Keychain/Keystore (`expo-secure-store`), never AsyncStorage/SharedPreferences in plain text.
- Expo **web** builds keep the session in localStorage (no httpOnly cookies from a static SPA). Accept only with a strict CSP, short-lived tokens and no third-party scripts; for sensitive web apps use the Next.js starter with server-side (cookie) sessions.
- No secrets embedded in the app binary. Certificate pinning only if threat model justifies it.
- Disable screenshots/app-switcher previews on sensitive screens (payments, IDs).
- Validate deep links; don't trust intent extras; declare minimal permissions.
- Release builds: obfuscation enabled (R8), debugging disabled, logs stripped.

## 5. AI features (if any)

- Treat model output as untrusted input: never execute it, never render as raw HTML, validate structured output.
- Defend against prompt injection from user content and fetched pages; keep system prompts free of secrets.
- Cap tokens/cost per user; log prompts responsibly (no personal data unless consented); human review for high-stakes outputs.
- Child-facing AI: strict content filters, no open-ended chat with strangers' content, parental visibility.

## 6. Process

- Threat model (15 min, STRIDE-lite) for every feature touching auth, money, personal data or user-generated content.
- `security-reviewer` agent runs on every PR touching those areas.
- Before launch: dependency audit clean, secrets scan clean, RLS/authorization tests green, headers verified (securityheaders.com), a manual abuse test of auth and payments.
- Have a breach plan: who is contacted, how keys are rotated, how users/regulators are notified within legal timelines.
