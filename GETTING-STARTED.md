# Getting started with MakerLine

Plain-language guide. The kit lives in `~/Documents/makerline` on your Mac.

---

## Part 1 — One-time setup (about 20 minutes)

Works on macOS today. The terminal parts also run on Linux; Windows is untested (use WSL).

### 0. Get the kit
```bash
git clone https://github.com/sairam5294/makerline ~/Documents/makerline
cd ~/Documents/makerline
```
Planning to contribute? Fork it on GitHub first and clone your fork instead. The rest of this guide assumes the kit is at `~/Documents/makerline`; any folder works, just adjust the paths.

### 1. Check your Mac has the basics
Open **Terminal** (Spotlight → "Terminal") and paste:
```bash
node -v && git --version && brew --version
```
- If `node` is missing or below v22: `brew install node`
- If `brew` is missing: install Homebrew from https://brew.sh
- Then: `brew install gh gitleaks` (GitHub tool + secret scanner)

### 2. Install the kit in your AI tools
**Claude Code** (recommended; updates with one command):
```bash
claude plugin marketplace add sairam5294/makerline
claude plugin install makerline@makerline
```
Later, `claude plugin marketplace update makerline` picks up new versions.

Only want the idea stage (no building)? Install `makerline-idea@makerline` instead — the same Idea Pack skills without the build phases. **Don't install both**: you'd see every skill twice (`/makerline:…` and `/makerline-idea:…`). If you did, remove `makerline-idea` under Customize → Plugins.

**Claude app (desktop / web) — easiest: add the repo as a marketplace** (once; updates come from GitHub):
1. Open **Customize** in the left sidebar → **Plugins**.
2. Choose **Add marketplace** and enter `sairam5294/makerline`.
3. Find **makerline** (or **makerline-idea**) in the list → **Install**.
4. Later: **Check for updates** on that marketplace, or turn on **Sync automatically**.
The marketplace installs whatever is on the `main` branch, so merge a release's pull request first.

**Claude app — from a file instead** (for a build that isn't on `main` yet):
```bash
./scripts/build-plugin.sh      # writes ../makerline.plugin (a zip file)
```
Then **Customize → Plugins → upload** and pick the file. Double-clicking the file or opening it in Finder does nothing — it has to be uploaded there. If the upload dialog greys it out, rename the copy to `makerline.zip` (it is a zip) and upload that. To replace an older version: open the installed plugin → **Remove**, then upload the new one.

Either way, Claude now knows the kit's skills (you'll see them as `/makerline:…`). Plugins installed in the Claude app are saved to your account, so the same skills are available in Claude Code too.

**Run everything with one command** (you don't need to call skills one by one):
- `/makerline:start` then your idea + *"give me everything"* → the whole Idea Pack in one go (add *"quick"* or *"deep"*).
- After you approve: `/makerline:start` *"set it all up"* → names + brand, stack, design system, full PRD, engineering docs and project setup in one go (it asks your picks once, up front).
- Then `/makerline:start` *"build it"* → one task at a time, each on its own branch.
- Idea Pack only: `/makerline-idea:start` + your idea.
You can also just type the idea in plain words — the kit's skills trigger on "I have a new idea…".

**Check it worked:** start a new chat and type `/makerline:` — the skill list should appear. In Claude Code: `claude plugin list` shows `makerline` with the version from the release.

**Cursor, Codex and Copilot** need nothing here: every project you create in Part 2 carries their rules (`.cursor/rules/`, `AGENTS.md`, `.github/copilot-instructions.md`). **ChatGPT** can't read your repo: paste the project's `docs/CONTEXT_PACK.md` into a ChatGPT project. Which tool to use for what: say *"make my tool plan"* (the `tool-plan` skill).

### 3. Fill in your profile (once)
Copy `owner/OWNER.example.md` to `owner/OWNER.md` (it is git-ignored, so your details stay private), then fill in hours per week, budget and which accounts you have (GitHub, Apple, Google Play, Supabase, Vercel…). Every new project copies it, so you're never asked twice.

### 4. Stay current
```bash
cd ~/Documents/makerline && git pull
```
Then re-run step 2's install (Claude Code: `claude plugin marketplace update makerline`) and, for existing projects, Part 3B.

---

## Part 2 — Starting a new idea

You can start in two ways. **Start with A** — no terminal needed.

### A. Thinking phases in the Claude app — the Idea Pack (no code yet)
1. In the Claude app, connect an empty folder for the idea (e.g. `~/Projects/bakery-orders`).
2. Say: **"I have a new idea: …"** (2–5 sentences). Or, to get everything in one go: **"Give me the full Idea Pack for this idea: …"**
3. Claude interviews you in short rounds → `PROJECT_BRIEF.md`, plus `CLARITY.md`: every open question with the decision it blocks.
   Add **"quick"** for a fast first look (~50–70k tokens: brief, short evaluation, top competitors, one-pager), or **"deep"** before you spend money.
4. It researches and writes an honest, constructive **evaluation** (`EVALUATION.md`): the strongest version of your idea, a reality check, the scorecard, users and market, a strengthening plan with a path to "Go", the tools and monthly cost, and **accessibility, inclusion and compliance** — who could be left out and what the law requires where you launch (AODA, ADA, the EU Accessibility Act, India's RPwD and more; the kit's baseline is accessible worldwide). Competitors get their own file (`COMPETITORS.md`): who leads, where they win, where you'd win, and whether your differentiator holds up.
5. **Design direction** (`DESIGN_DIRECTION.md`): experience principles, flows, a screen list, 2–3 visual directions, and clickable grey-box **wireframes** in `design/wireframes/index.html` (open it in a browser; "Prototype" clicks through). With the Figma connector, it can build them in Figma too.
6. **Draft PRD** (`PRD.md` v0): goals and metrics, personas, scope, user stories, risks and a release plan.
7. A **one-pager** (`ONE_PAGER.md`) and an index (`docs/product/README.md`) tie it together.
8. You push back, refine, repeat. Optionally run a cheap **validation test** — the wireframes are the prototype.
9. When you're convinced: **you approve**. In the Claude app, say "I approve the evaluation" — Claude records your exact words. (From a terminal it's `scripts/approve.sh`.)

Then naming, tech stack, design system, the full PRD and the plan also work in the Claude app — they're documents.

### B. Building phases (code) — use Claude Code, Cursor or Codex
Create the project folder with the kit's starter (in Terminal):
```bash
cd ~/Documents/makerline
./scripts/new-project.sh ~/Projects/bakery-orders --starter   # phone app (iOS + Android + web)
# or
./scripts/new-project.sh ~/Projects/bakery-site --web         # website / landing page
```
If you already did Part A in that folder, it only adds the missing files — your docs are kept.

Then, once:
```bash
cd ~/Projects/bakery-orders
npm install
cp .env.example .env.local        # add keys later (Supabase etc.)
scripts/setup-github.sh           # private GitHub repo (optional but recommended)
npx lefthook install              # turns on the safety checks for commits
npm run dev                       # see the app: press w for web, or scan the QR code with Expo Go
```

Open the folder in **Claude Code, Cursor or Codex** and just talk to it:

| You say | What happens |
|---|---|
| "Where are we? What's next?" | Reads STATUS/HANDOFF, tells you the phase and next step |
| "Build the next task" | Builds one task from PLAN.md with tests, runs checks, commits on a branch |
| "Review this" | Accessibility, UX, security, code and test review → report with fixes |
| "Does it match the Figma?" + link | Design QA against your Figma frame |
| "We're adding an AI feature" | Runs ai-feature: when to use AI, UX, evals, cost |
| "Handoff" (end of every session) | Saves where you stopped so any tool can continue |
| "Show my portfolio" | All projects, their phase, blockers, costs |

**The one rule:** only **you** approve the evaluation (`scripts/approve.sh`). Until then the tools won't write app code.

### Which tool when
- **Claude app (Cowork):** ideas, interviews, evaluation, planning, documents.
- **Claude Code:** building features, reviews (strongest safety checks).
- **Cursor:** visual UI tweaks with live preview.
- **Codex:** well-defined separate tasks (tests, small features) in parallel.
All of them read the same `AGENTS.md` and `docs/product/` — switch any time, just say "handoff" before switching.

---

## Part 3 — Updating

### A. Update the kit itself (improve a skill, rule or starter)
Easiest: open `~/Documents/makerline` in **Claude Code** and ask, e.g.
> "Update MakerLine: the evaluation report should also include a pricing page benchmark. Then release it as 0.6.0."

Claude edits the files in `plugin/` and runs the release. Or do it yourself:
1. Edit files in **`plugin/`** only (never edit `template/.agents` — it's generated).
2. Release:
   ```bash
   cd ~/Documents/makerline
   ./scripts/release-kit.sh 0.6.0 "What changed, in one line"
   ```
   This copies changes into the template, runs the kit tests, sets the version, adds a CHANGELOG line, rebuilds `~/Documents/makerline.plugin`, and commits.
3. **Reinstall the plugin in Claude**: Claude Code → `claude plugin marketplace update makerline` (after you push); Claude app → open the new `makerline.plugin` → Install.
4. If the kit is on GitHub: `git push` (CI checks everything again).
5. If you changed a skill, the monthly evals (3rd of each month) will tell you if it got worse. To check now: in Claude Code say "Run the kit evals following evals/RUNBOOK.md".

### B. Bring an existing project up to the new kit version
```bash
cd ~/Documents/makerline
./scripts/upgrade-project.sh ~/Projects/bakery-orders          # preview only
./scripts/upgrade-project.sh ~/Projects/bakery-orders --apply  # do it
```
Kit files (skills, agents, rules, hooks) are replaced, with backups. **Your** files (AGENTS.md, settings, code, docs) are never overwritten — the output lists differences; ask your AI tool to "merge the MakerLine template changes into AGENTS.md".

**Adopting a project that was built before the kit** (any stack, including Python): run the same command. The script notices the project has never seen the kit and switches to *adopt mode*: nothing that exists is overwritten (your CI, rules and scripts stay, and are listed in `.product-kit-keep` so later upgrades leave them alone), missing kit files are added, and `docs/product/STATUS.md` is created marked approved-by-adoption so the review, test and ship skills start from where the project really is. It warns if your `.gitignore` hides anything it added or if you already use another hook manager.

### C. Update standards (laws, WCAG, store rules)
Every quarter a scheduled report arrives by email/phone. Open the kit in Claude Code and say:
> "Run standards-refresh with this report: <paste>". Then release (A.2).

### D. Update design tokens (colours, spacing)
Change them in Figma (the "MakerLine — Design System" file or your product's copy) or in `design/tokens.json`, then in the project:
```bash
npm run tokens && npm run contrast
```
Or ask Claude: "Sync my Figma variables to design/tokens.json".

### E. Update app libraries (Expo, Next.js, packages)
- GitHub sends weekly **Dependabot** pull requests — CI tests them; merge when green.
- Big upgrades (e.g. new Expo SDK): ask Claude Code "upgrade Expo to the latest SDK following the official upgrade guide", then run `npm run check`.

---

## If something goes wrong
- "Blocked by MakerLine approval gate" → you haven't approved yet (`scripts/approve.sh`).
- "Blocked by safety hook" → the AI tried something risky (delete, force-push, read secrets). Good. Do it yourself if you really mean it.
- Commit refused → read the message: usually a leaked key, lint error or the approval gate.
- Lost track → "Where are we?" or `python3 ~/Documents/makerline/scripts/portfolio.py` and open `portfolio/index.html`.
