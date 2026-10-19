# Rules — {{product}}

_Updated {{date}} · Standing rules for every AI tool and person working here. Short on purpose; details live in `AGENTS.md` and `.agents/skills/product-standards/references/`. When a rule here and a prompt disagree, the rule wins unless the owner changes it in `docs/product/DECISIONS.md`._

## Always
1. Start by reading `docs/product/HANDOFF.md`, `STATUS.md`, this file and `docs/MEMORY.md`. Then only what the task needs.
2. One task per session and per branch (`scripts/branch.sh <type> "<summary>"`). End with `handoff`.
3. Run `{{npm run check}}` before saying "done". Never weaken a test to pass.
4. Ask before: adding a dependency, deleting data, force-push, production settings, paid services, anything irreversible.
5. Log decisions in `docs/product/DECISIONS.md`; update `STATUS.md` after each task.

## Tokens (`context-budget.md`)
- Search before reading; read file ranges, not whole files; never read `node_modules`, lockfiles, build output, generated native folders, large media.
- Reviewers and researchers run as subagents and return ≤ 300 words; they get the diff + one standard file, not the repo.
- Keep living docs short: HANDOFF ≤ 40 lines, STATUS ≤ 60, MEMORY ≤ 60, AGENTS.md ≤ 120.
- When a session gets long or changes topic: `handoff`, then start fresh.
- Mechanical work (renames, formatting, simple tests) on the faster model; planning, evaluation, security review on the strongest.

## Security (`security.md`, `SECURITY.md`)
- Server-side authorization on every read and write; RLS on every user-data table: `{{list the project's tables}}`.
- Schema-validate every input on the server; parameterized queries only; output-encode.
- No secrets in code, logs, prompts or client bundles; only `{{anon/publishable}}` keys on the client; `.env.example` is the only env file committed.
- Rate limits on `{{auth, OTP, search, AI, uploads}}`; fail closed on errors.
- New dependency = verified name on the registry + reason in DECISIONS.md. Actions pinned to SHAs.

## AI features (`ai.md`)
- All model calls server-side; user content is data, never instructions; tool permissions minimal.
- AI output labelled; user can see, edit, undo or opt out; a non-AI path exists for the core task.
- Prompt and model versions pinned; eval set runs in CI before launch and after prompt changes; cost cap `{{₹/$ per user per month}}` with alerts.
- Use current models and APIs — check official docs for what's current before choosing (`standards-refresh` keeps `ai.md` up to date); never invent model names, endpoints or packages.

## Accessibility and inclusion (`accessibility.md`, `inclusion.md`)
- WCAG 2.2 AA everywhere; accessible worldwide and non-discriminatory whatever the launch market; plus `{{laws in scope from EVALUATION §11}}`.
- Every screen: five states, accessible names, focus order, 44pt/48dp targets, 200% text, reduced motion.
- Accessibility statement and barrier-feedback route from the first public release.

## Privacy (`privacy.md`)
- Minimum data; `DATABASE.md` is the personal-data inventory; export and delete work; `{{DPDP / GDPR …}}` obligations listed in `SECURITY.md` §5.

## Never
- Write `Evaluation: APPROVED` yourself · push to `main` · commit `.env` · store card or ID numbers · log personal data · ship a screen without its error and empty states · disable font scaling · add a CAPTCHA puzzle without an alternative · use raw colours or sizes outside tokens.
