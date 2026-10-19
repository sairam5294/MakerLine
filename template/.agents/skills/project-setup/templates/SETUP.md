# Setup — {{Name}}

_Updated {{date}}. Every step shows the command and what you should see. Stuck? See "Common problems" at the end._

## 0. First time only — the repo has docs but no code yet
Create the app from the kit starter into this folder (existing docs are kept): `{{~/Documents/product-kit/scripts/new-project.sh . --web}}` (or `--starter` for the Expo app). Then continue from step 3.

## 1. Prerequisites
| Tool | Version | Check | Install |
|---|---|---|---|
| Git | any recent | `git --version` | {{macOS: `xcode-select --install`}} |
| {{Node.js}} | {{22 LTS}} | `node -v` → `v22.x` | {{nvm / nodejs.org}} |
| {{pnpm / npm}} | {{…}} | `{{pnpm -v}}` | {{`corepack enable`}} |
| {{Supabase CLI / Docker}} | {{…}} | `{{supabase -v}}` | {{…}} |
| {{Expo Go / Xcode / Android Studio}} | {{only for mobile}} | | |

## 2. Get the code
**Option A — clone (recommended):**
```bash
git clone https://github.com/{{owner}}/{{repo}}.git
cd {{repo}}
```
**Option B — GitHub CLI:** `gh repo clone {{owner}}/{{repo}} && cd {{repo}}`

**Option C — Download ZIP** (GitHub → Code → Download ZIP), then unzip and `cd` into the folder. A ZIP has no git history and no git hooks. To contribute, run `git init && git remote add origin https://github.com/{{owner}}/{{repo}}.git && git fetch && git reset origin/main`, or clone instead.

## 3. Install
```bash
{{install command}}
{{npx lefthook install}}   # git hooks: secret scan, branch-name check, checks before push
```
You should see: {{"added N packages" with no errors}}.

## 4. Environment variables
```bash
cp .env.example .env.local
```
Open `.env.local` and fill each value; the comment above every line says what it is and where to find it. Never commit `.env.local`.

## 5. Local database and services
```bash
{{npx supabase start}}          # first run downloads images, takes a few minutes
{{npx supabase db reset}}       # applies migrations and seed data
```
You should see: {{API URL and anon key printed — paste into .env.local}}.

## 6. Run it
```bash
{{npm run dev}}
```
Open {{http://localhost:3000}}. You should see: {{the home screen with seed data}}.
{{Mobile: press `i` / `a` or scan the QR code with Expo Go.}}

## 7. Test it
```bash
{{npm run check}}        # typecheck + lint + unit tests
{{npm run test:e2e}}     # end-to-end + accessibility (axe)
```

## 8. Deploy
- **Preview:** every pull request gets a preview deployment ({{Vercel GitHub integration}}); its link appears on the PR.
- **Production:** merging to `main` deploys to {{production URL}}. Production env values live in {{Vercel → Project → Settings → Environment Variables}} and {{Supabase → Project Settings}}.
- **Database migrations in production:** {{`npx supabase db push` from CI / manual step}} — always after a backup.
- **Rollback:** {{Vercel → Deployments → previous → Promote to Production}}; database: restore the backup taken before the migration.

## 9. Common problems
| Symptom | Cause | Fix |
|---|---|---|
| `command not found: {{pnpm}}` | not installed | `corepack enable` |
| App starts but shows "Missing env var X" | `.env.local` incomplete | compare with `.env.example` |
| Push refused: branch name | convention | `scripts/branch.sh fix "what changed"` |
| {{Port 3000 in use}} | another app | `{{PORT=3001 npm run dev}}` |
