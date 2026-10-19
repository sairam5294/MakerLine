# GitHub rules — {{Name}}

_Updated {{date}} · Free-tier limits checked {{date}} against GitHub, Vercel and Supabase pages ({{links}}). Re-checked by standards-refresh._

## 1. Branches
- Name: `<type>/<Mon>-<DD>-<summary>` — `scripts/branch.sh <type> "<summary>"`. Types: feat · fix · content · design · security · a11y · docs · test · ci · deps · refactor · perf · chore · release · **exp**.
- **Experiment branches** (`exp/…`): for spikes and "will this work?". Never merged directly — if it works, redo it cleanly on a `feat/` branch. Expire after 14 days; listed by the monthly repo-health report.
- `main` is always deployable and protected: no direct pushes, PR + green checks required.
- Merged branches are deleted automatically (repo Settings → General → "Automatically delete head branches" ✓). Unmerged branches older than 30 days appear in the repo-health report; the owner decides — nothing is deleted automatically.

## 2. Pull requests
- One task (PLAN.md T-xx) per PR; aim for < 400 changed lines. Bigger → split.
- Title = what changed in plain words. Body (template): what & why, how to check, checklist. Screenshots light + dark for UI.
- Draft PR early to get a preview deployment; mark Ready when checks are green.
- Required checks: CI (gate, secrets, typecheck, lint, tests, e2e + axe), branch name. AI review runs on non-draft PRs.
- Review: owner reviews every PR; for auth, payments, personal data or AI features run `quality-review` first.

## 3. Merge strategy
- **Squash and merge** (repo setting: allow squash only). One commit per PR on `main`, message = PR title + `(#n)`.
- Rebase on `main` before merging if the branch is behind (`git pull --rebase origin main`); never force-push `main`.
- Release tags `vX.Y.Z` on `main` with notes from merged PR titles.

## 4. Previews and deployments
- Every PR gets a preview deployment ({{Vercel GitHub integration}}); its URL is posted on the PR. Preview env vars point at a {{staging/preview}} database or seed data — never production data.
- Production deploys only from `main`.
- **Retention:** keep production deployments for rollback ({{last N}}); previews of closed PRs are removed by the host after {{n}} days (Vercel → Settings → Deployment Retention). Actions artifacts: `retention-days: 7` on every upload step.

## 5. Storage and usage monitoring
| Resource | Free-tier limit (checked {{date}}) | Watch | Action at 80% |
|---|---|---|---|
| Repo size | {{soft limit}} | repo-health report | remove large files (history rewrite needs the owner's approval) |
| GitHub Actions minutes / storage | {{…}} | Settings → Billing | cut matrix, cache deps, shorter retention |
| Git LFS | {{…}} | — | don't use LFS for design files; keep them in Figma |
| Vercel bandwidth / builds | {{…}} | Vercel → Usage | image optimisation, ignore-build for docs-only PRs |
| Supabase DB / storage / egress | {{…}} | Supabase → Usage | archive old rows, compress uploads |
`repo-health.yml` writes a monthly summary (repo size, Actions storage, branches > 30 days, PRs open > 14 days). Read-only: it reports, never deletes.

## 6. Dependencies and security
- Dependabot weekly, minor/patch grouped; majors one at a time with a test run.
- Secret scanning + push protection on (Settings → Code security). gitleaks in pre-commit and CI.
- Actions pinned to commit SHAs; `permissions:` least privilege in every workflow.

## 7. Issues and labels
- Labels: `bug`, `a11y`, `security`, `feature`, `chore`, `blocked`, `good first issue`. Bugs include steps, expected, actual, device/browser, assistive tech if relevant.
