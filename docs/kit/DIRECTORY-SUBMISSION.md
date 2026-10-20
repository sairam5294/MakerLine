# Directory submission pack: makerline-idea

Everything needed to submit the **makerline-idea** plugin to Anthropic's plugin directory, the catalog people browse inside Claude and on [Claude Marketplace](https://claude.com/marketplace/plugins). Idea-pack goes first because it is the easier first ask for strangers: documents only, no code, no hooks, nothing to set up. Submit **makerline** later, as its own submission, using the same pack.

_Researched 2026-10-20. **Confirmed** = read on an Anthropic page linked here. **Unconfirmed** = not stated on any page found; our choice or a guess. Re-check the linked pages before submitting: the process changed recently (the old Console form is retired)._

## 1. How submission works (confirmed)

| Fact | Source |
|---|---|
| Submit at the developer portal: [claude.ai/directory/manage](https://claude.ai/directory/manage) → **Submit new** → **Plugin bundle**. The earlier Claude Console form is no longer supported. | [Publish to the directory](https://claude.com/docs/directory/publish) |
| Who can submit: a paid plan (Pro, Max, Team or Enterprise). Free accounts can't. On Pro and Max you submit from your own account. The listing belongs to the organization that submits it first. | [Publish to the directory](https://claude.com/docs/directory/publish) |
| Source is a GitHub repository. It can be private while validating, but must be **public before the listing goes live**. Your GitHub account must be connected on claude.ai. | [Submit a plugin](https://claude.com/docs/plugins/submit) |
| The form has 5 steps: **Source** (repository, plugin path, branch or tag, then **Validate**) → **Listing details** (no input fields: name and description are read from `plugin.json` and the README) → **Data handling** (4 questions) → **Compliance** (contact email + 4 acknowledgements) → **Review and submit** (update method: GitHub push webhook or scheduled check; auto-publish toggle). | [Submit a plugin](https://claude.com/docs/plugins/submit) |
| One submission per plugin folder. In a repository with several plugins, validate and submit each folder on its own. The repository and folder can't be changed after submitting. Limit: 10 submissions per organization per 24 hours (drafts count). | [Submit a plugin](https://claude.com/docs/plugins/submit), [Pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist) |
| Every version gets automated validation and a security scan; a person reviews a **new** listing before it goes live. Review time isn't fixed. | [Publish to the directory](https://claude.com/docs/directory/publish) |
| After listing, merging to the tracked branch publishes new versions (scanned first). Raise `version` in `plugin.json` with every release. | [Submit a plugin](https://claude.com/docs/plugins/submit) |
| Every listing must follow the [Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms) and [Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy). | [Publish to the directory](https://claude.com/docs/directory/publish) |
| The policy also asks for: documentation of how it works and how to troubleshoot; verified support contact; a privacy policy link for software that collects data or connects to a remote service; **at least three working example prompts**; a test account with sample data; skills with no hidden or remotely fetched instructions; descriptions that match what the plugin actually does. | [Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy) |

**Not found on any page (unconfirmed):** screenshot or icon requirements and sizes, a category picker, a demo-video field, review timelines, and the wording of the four compliance acknowledgements. Prepare the media in sections 6 and 7 anyway: they serve the README, the docs site, the GitHub social preview and any form field that turns out to exist.

## 2. Source step: what to enter

| Field | Value |
|---|---|
| Repository | `sairam5294/product-kit` |
| Plugin path | `makerline-idea` (the folder holding `.claude-plugin/plugin.json`) |
| Branch or tag | `main` (the marketplace install already tracks `main`) |
| Update method | GitHub push webhook (needs admin access to the repo, which the owner has) |
| Auto-publish passing versions | Off for the first month; turn on once two updates have gone through cleanly. _(Our choice.)_ |

## 3. Listing text

The portal reads the listing from `makerline-idea/.claude-plugin/plugin.json` (name, description) and `makerline-idea/README.md` (shown as the listing's description). Both are **generated** from `plugin/` by `scripts/build-idea-pack.py`, so change the generator or the source, never the copy, then re-validate.

**Name:** `makerline-idea` (display: Idea Pack) · **Author:** Sairam Mogullapalli · **Licence:** MIT

**One line (≤ 80 characters):**
> Decide if a product idea is worth building, before you write any code.

**Short (≤ 200 characters, fits `plugin.json` description):**
> Turn a product idea into an honest evaluation, real competitors, wireframes, a draft PRD and a one-pager. Accessibility and compliance included. No code; just documents in your folder.

**Long (the opening of the README):**
> Idea Pack turns a few sentences about a product idea into everything you need to decide whether to build it. It interviews you briefly, researches the market, and writes an honest, constructive evaluation: the strongest version of your idea, a reality check, a scorecard with sources, real competitors and a test of your differentiator, and a path to "Go". It asks who the idea could leave out and which accessibility and privacy laws apply where you launch. At the Standard depth it adds a design direction with clickable low-fi wireframes and a draft PRD. Everything lands as plain Markdown and HTML files in the folder you connect, checked by a script before you see it. You decide: go, change or stop. Made by a UX designer for designers and solo makers who build with AI. Part of the open-source MakerLine.

**Keywords** (already in `plugin.json`): idea, discovery, evaluation, competitors, prd, wireframes, accessibility. Consider adding `product-management` and `ux`.
**Category:** Product management / Design. _Unconfirmed: no category field was found; Anthropic may assign placement during review._

## 4. Five example prompts

The policy asks for at least three working prompts ([policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)). Each one should be re-run on a fresh account before submitting (checklist, section 11).

1. `/makerline-idea:start — Give me everything for this idea, quick: a booking app for small physio clinics so patients can rebook from a text message.`
2. `I have a new idea: a meal-planning app for families where one person has diabetes.` (the discovery interview)
3. `Who are my competitors and is my differentiator real?` (after a brief exists)
4. `What would it look like?` (design direction and clickable wireframes)
5. `Make my tool plan — I have Claude Pro and ChatGPT Plus, and 6 hours a week.`

**Test sample data** (policy 3D asks for a test account with sample data): makerline-idea needs no account. Point reviewers at the public brief `evals/cases/community-amenities/PROJECT_BRIEF.md` and the finished output in `examples/idea-pack-clubslot/` so they can compare a run with a known-good pack.

## 5. Data handling answers

The four questions on the Data handling step, as listed in [Submit a plugin](https://claude.com/docs/plugins/submit). Exact wording is only visible in the portal.

| Question | Answer | Notes for the reviewer |
|---|---|---|
| Does the plugin read or store personal data? | **No personal data is collected by the plugin.** It reads and writes only files in the folder the user connects. | The user's idea and answers stay in their Claude conversation and their own folder (`docs/product/`, `design/`). The new-idea interview saves the user's own answers about their hours, budget and tools to `docs/product/OWNER.md` in that folder, so they aren't asked twice. |
| Does it send data to services other than its declared connectors? | **No.** | Research uses Claude's own web search and fetch tools; queries describe the market and competitors, not the user. The bundled `check_idea_pack.py` imports only the Python standard library and makes no network requests. No telemetry, no analytics, no server of its own. |
| How long does it keep data? | **It keeps nothing.** | Files live in the user's folder until the user deletes them. |
| Is it intended for people under 18? | **No.** | Audience: designers and solo makers planning products. |

**Connectors** (`makerline-idea/.mcp.json`): GitHub, Figma, Vercel, Supabase, Notion, Linear, all remote `https://` servers. They are opt-in: connecting each is the user's choice in the plugin's Connectors settings, every skill works without them, and `CONNECTORS.md` lists them. A connector reads first and writes only when asked in chat. _Unconfirmed: whether all six are approved directory connectors (policy 3F lets plugins connect to "any Connector approved in the Software Directory"). Check each in the directory before submitting._

**Privacy policy link:** https://sairam5294.github.io/product-kit/privacy.html (source: `docs/site/privacy.md`).

## 6. Permissions and what the plugin runs

| Component | What it can do | Why |
|---|---|---|
| 9 skills (`skills/*/SKILL.md`) | Instructions only; read and write Markdown and HTML in the connected folder | The Idea Pack phases |
| 4 agents (`market-researcher`, `devils-advocate`, `idea-champion`, `accessibility-strategist`) | Tools: Read, Grep, Glob, WebSearch, WebFetch; three also list Bash | Research and the four evaluation perspectives; Bash runs the checker |
| `skills/idea-pack/scripts/check_idea_pack.py` | Reads the pack's files, prints pass, warn or fail; standard library only, no network | Checks the pack before the user sees it. SKILL.md tells Claude to run it; no hook runs it, so the "scripts the validator couldn't follow" hold should not apply ([checklist](https://claude.com/docs/plugins/pre-submission-checklist)) |
| `.mcp.json` | Six remote MCP servers, no credentials in the file | Optional connectors |
| Hooks | **None** in makerline-idea | The approval gate hooks live in projects made with the full kit |

## 7. Safety notes

- **Approval gate.** Nothing is built from the Idea Pack: it writes documents only. The full kit's gate (no app code until the owner writes `Evaluation: APPROVED` with `scripts/approve.sh`) is enforced by hooks, git hooks and CI in projects, and AI tools cannot write that line themselves.
- **No secrets.** No keys or tokens in any file; `.mcp.json` has URLs only. `CONNECTORS.md` rule: secrets, keys and users' personal data never go into prompts or documents.
- **Honest output.** Evidence, estimate and opinion are labelled; unknowns become open questions in `CLARITY.md` instead of guesses; the accessibility-law section is marked "Not legal advice".
- **Readable instructions.** All guidance is plain Markdown in the plugin folder; nothing is fetched at runtime as instructions (policy 2F, 2G).
- **No restricted categories.** No payments, ads, or image, video or audio generation (wireframes are design aids, which the policy allows).

## 7b. Icon

`docs/kit/brand/makerline-idea-icon.svg` (+ `-512.png`, `-32.png`): a white spark on approval green, the sibling of MakerLine's check-mark icon (`makerline-icon.svg`, also the docs site favicon). Readable at 16 px; contrast white on #17694A is 6.5:1. The directory may not ask for an icon (none found in its requirements); use it for the social preview and the README.

## 8. Screenshots to capture

**Ready (2026-10-20):** 2–8 are in `docs/kit/submission-assets/` (`2-one-pager.png` … `8-social.png`), rendered from the ClubSlot example so every number is real. Still to capture yourself: **1** (the Claude app conversation).

_Sizes are our choice (no requirement found). Use 1600 × 1000 PNG (16:10), light mode, plus one dark-mode shot; the 1280 × 640 GitHub social preview is GitHub's recommended size. Write alt text for every image; never let text in an image be the only place a fact appears._

| # | What to capture | Alt text |
|---|---|---|
| 1 | Claude app: the `/makerline-idea:start … quick` prompt and the first question round | Claude asking three short discovery questions about a physio-booking idea |
| 2 | `ONE_PAGER.md` rendered, verdict line visible | One-page summary with a "Go with changes" verdict, competitors and the next test |
| 3 | `EVALUATION.md` scorecard table | Scorecard: eight dimensions with scores, evidence and how to raise each |
| 4 | `COMPETITORS.md` differentiator test | Differentiator test table comparing the idea with three competitors |
| 5 | Wireframes in a browser, prototype mode, phone frame | Clickable grey-box wireframe of a booking screen with large slot buttons |
| 6 | Accessibility section: "Who could be excluded" table | Table of groups who could be excluded and the design response for each |
| 7 | Folder view of `docs/product/` after a Standard run | File list: one-pager, brief, clarity log, evaluation, competitors, PRD |
| 8 | Social preview (1280 × 640): name, one line, "by Sairam Mogullapalli" | Idea Pack: decide if a product idea is worth building, before you write any code |

Use the ClubSlot example for 3–6 so every number shown is real. If images go into the plugin's README, they must be PNG, JPEG, GIF or WebP files inside `makerline-idea/`, shown with Markdown image syntax ([checklist](https://claude.com/docs/plugins/pre-submission-checklist)).

## 9. 90-second demo script

Screen recording at 1920 × 1080, captions burned in **and** a caption file (`.srt`), no music under the voiceover. Read slowly: about 200 words.

| Time | Shot | Voiceover |
|---|---|---|
| 0:00–0:08 | Title card: "Idea Pack", one line, author | "You have an idea. Before you spend weeks building it, spend five minutes finding out if it's worth it." |
| 0:08–0:20 | Claude app → Customize → Plugins → Add marketplace → Install makerline-idea | "Idea Pack is a free, open-source Claude plugin. Install it once from the Plugins menu." |
| 0:20–0:32 | New chat, connect an empty folder, type the quick prompt | "Connect an empty folder, type your idea and the word 'quick'." |
| 0:32–0:42 | Claude asks a short question round; user replies "just do it" | "It asks a few questions. Don't know an answer? Say 'just do it' and it marks a default for you to confirm later." |
| 0:42–0:58 | Research running; then the one-pager opens, zoom on the verdict | "It researches real competitors and writes an honest verdict, with the strongest version of your idea and the biggest risks, in plain words." |
| 0:58–1:10 | Scroll to accessibility table, then the Standard run's wireframes clicking through | "It asks who your idea could leave out and what the law expects where you launch. Go deeper and you get clickable wireframes and a draft PRD." |
| 1:10–1:22 | Finder/Explorer showing the files | "Everything is plain files in your folder. No account, no tracking, no server." |
| 1:22–1:30 | End card: "Try it: /makerline-idea:start" + docs site URL + "Created by Sairam Mogullapalli" | "Go, change, or stop: you decide. Try Idea Pack today." |

## 10. Support, versioning, ownership

- **Support contact:** GitHub issues, https://github.com/sairam5294/product-kit/issues/new/choose (forms for bugs, skill requests, standards drift and accessibility barriers). Security: private reporting per `SECURITY.md` (acknowledged within 7 days).
- **Compliance contact email:** the owner's own email, entered in the portal only; don't publish it in the repo.
- **Versioning:** `MAJOR.MINOR.PATCH`, currently 0.11.0, the same number in both plugins. `scripts/release-kit.sh` bumps it and then runs `build-idea-pack.py`, which copies the kit's version into `makerline-idea/.claude-plugin/plugin.json`. Raise it with every release; the directory docs ask for this.
- **Ownership:** submit from the owner's personal Pro account; the first organization to submit a folder owns the listing.

## 11. Pre-submission checklist

**Validate**
- [x] `claude plugin validate ./makerline-idea` prints "Validation passed" (passed 2026-10-20)
- [x] `claude plugin validate ./plugin` and `claude plugin validate .` (marketplace) also pass (passed 2026-10-20)
- [ ] Portal **Validate** on `makerline-idea`: no **Blocking** findings; read every **Policy hold** and **Warning**
- [x] `version` raised since the last published version

**Things the portal checks that are worth fixing first** ([checklist](https://claude.com/docs/plugins/pre-submission-checklist))
- [ ] Name: `makerline-idea` is made of generic words. Generic-only names can be **held for a reviewer** ("Name may be confused with an existing listing"). Decide before submitting, because the folder and name are fixed afterwards: keep it, or rename to something distinctive such as `makerline-makerline-idea` (this changes install commands in README, GETTING-STARTED and the site). _Unconfirmed whether another listing already uses the name: search the directory first._
- [x] Trim `makerline-idea/CONNECTORS.md` and `.mcp.json` to what makerline-idea's skills use (done in 0.12.0: own 3-connector list) (GitHub, Figma, Notion). Today both are copies of the full kit's and list skills makerline-idea doesn't contain; the policy requires descriptions to match functionality. Change it in `scripts/build-idea-pack.py`.
- [x] Add a short "What it runs and sends" section to the makerline-idea README (web search, `check_idea_pack.py`, optional connectors, no telemetry). The scan looks for undisclosed behaviour, and the README is where it's disclosed.
- [x] No `.DS_Store`, symlinks, binaries, or files over 256 KiB in `makerline-idea/` (checked 2026-10-20: 57 files, none over 250 KB, no binaries)
- [x] README at least 40 words outside code blocks; `license` set in `plugin.json` (both true today)

**Fresh-account install test**
- [ ] On a second Claude account (or a clean profile) with no kit installed: add the marketplace, install makerline-idea, type `/makerline-idea:` and see the skills
- [ ] Run all five prompts in section 4 in an empty folder; each finishes, and `check_idea_pack.py` passes
- [x] Repeat in Claude Code with `claude plugin install makerline-idea@makerline` (verified 2026-10-20 on a clean profile: marketplace add + install → makerline-idea 0.12.0 enabled)
- [x] With no connectors connected, nothing asks the user to connect one (verified in three blind Quick runs, 2026-10-20)
- [ ] Optional: `claude plugin eval` to compare output with and without the plugin ([checklist](https://claude.com/docs/plugins/pre-submission-checklist))

**Renders and reads well**
- [ ] `makerline-idea/README.md` renders on GitHub: tables, links and the `CONNECTORS.md` link work
- [x] Docs site builds (`python3 scripts/build-site.py`) and the privacy page is live
- [ ] Every screenshot has alt text; the demo has captions

**Legal and credit**
- [x] `LICENSE` (MIT) at the repo root; `"license": "MIT"` in `plugin.json`
- [x] `author.name` is "Sairam Mogullapalli" in `plugin.json` and the marketplace file; README ends with the credit line
- [x] Nothing presents the plugin as official or Anthropic-made; no third-party logos in screenshots beyond what's on screen (grep for "official"/"Anthropic" claims: none)
- [x] Repository is **public** before the listing goes live

## 12. After submitting

- Track status in the portal ([Track your submission](https://claude.com/docs/directory/submission-status)). A "Policy hold" is not a rejection.
- Once live, add the directory link to the README, the docs site and the release notes, and add directory usage to the monthly kit retro (`docs/kit/KIT-RETRO.md`).
- Then repeat this pack for `plugin` (makerline). Its hooks and larger scope make a hold more likely, so expect a longer review.
