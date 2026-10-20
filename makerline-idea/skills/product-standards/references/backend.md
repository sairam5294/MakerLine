# Backend, API & Server Standard

Default philosophy for a small team: **managed services first** (auth, database, storage, hosting), custom servers only when needed. Less infrastructure = fewer outages and security holes.

## 1. Architecture defaults

- Start as a modular monolith (one backend, clear feature modules). No microservices before product-market fit.
- Backend-as-a-service (Supabase / Firebase) or serverless functions (Vercel, Supabase Edge Functions, Cloudflare Workers) for most MVPs.
- Keep secrets and privileged logic (payments, admin, AI calls with paid keys) on the server only.

## 2. API design

- REST with resource nouns (`/lessons/:id`) or typed RPC (tRPC / server actions); pick one and be consistent.
- Consistent JSON error shape: `{ "error": { "code": "LESSON_NOT_FOUND", "message": "…", "details": {} } }` with correct HTTP status (400 validation, 401 unauthenticated, 403 forbidden, 404, 409 conflict, 422, 429 rate-limited, 5xx server).
- Version public APIs (`/v1`); never break mobile clients — old app versions stay in the wild for months. Add fields; don't rename/remove without a deprecation window. Support a "minimum supported app version" check.
- Pagination (cursor-based for feeds), filtering and sorting via query params; cap limits.
- Idempotency keys for payments and any retried POST.
- Document with OpenAPI or shared TypeScript types.

## 3. Data

- Relational (Postgres) by default; model data explicitly with foreign keys and constraints — the database enforces integrity, not just the app.
- Migrations are versioned in git and applied via CI; never edit production schema by hand.
- Row-level security on every table holding user data; policies tested.
- Timestamps in UTC (`timestamptz`); convert to local time only in the UI.
- Soft-delete only where recovery is a product need; honour hard-delete for privacy requests.
- Daily automated backups with tested restore (restore once before launch).
- Index columns used in filters/joins; watch slow-query logs.

## 4. Reliability & operations

- Environments: local → preview (per PR) → production. Separate databases and keys per environment.
- Health check endpoint; uptime monitor (e.g. Better Stack, UptimeRobot).
- Error tracking (Sentry) on client and server with release tags and source maps.
- Structured logs (JSON) with request IDs; no personal data or secrets in logs.
- Timeouts and retries with backoff on every outbound call; circuit-break flaky third parties.
- Background jobs/queues for slow work (emails, media processing, AI) — keep request handlers fast (< 500 ms p95 target).
- Feature flags for risky launches; ability to roll back a deploy in one click.

## 5. Cost control

- Set billing alerts on every provider on day one.
- Cache aggressively (CDN for static/media, HTTP caching headers, query caching).
- Media: compress and transcode; serve via CDN; stream audio/video rather than download whole files when possible.
- AI/API calls: cache results, cap per-user usage, pick the cheapest model that passes quality checks.

## 6. Notifications & email

- Transactional email via a provider (Resend, Postmark, SES) with SPF/DKIM/DMARC configured.
- Push notifications via Expo Notifications / FCM / APNs; users control categories; respect quiet hours.
