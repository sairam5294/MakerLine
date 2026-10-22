# MakerLine launch kit

Ready-to-post drafts for launching MakerLine. Edit them into your own voice before posting; nothing here is posted automatically. Every number is real and sourced from the repo: 25 skills, 14 agents, the ClubSlot and RhythmBuddy runs, and the token figures in `evals/results.md`.

**Links to use everywhere**

- Site: https://sairam5294.github.io/makerline/
- Repo: https://github.com/sairam5294/makerline
- Install: `claude plugin marketplace add sairam5294/makerline`
- Media: `docs/kit/brand/makerline-demo.gif` (plays once, about 9 seconds), `makerline-social-preview.png` (1280 × 640), screenshots in `docs/kit/submission-assets/`

## Order of launch

1. **Day 0:** merge the latest release, check the site in both themes and on your phone, and submit MakerLine Idea to the Claude plugin directory (`DIRECTORY-SUBMISSION.md`).
2. **Day 1:** LinkedIn post (below), with the demo GIF.
3. **Day 3:** the long article on Medium or your portfolio, linked from LinkedIn.
4. **Once the directory listing is live:** Product Hunt, on a Tuesday to Thursday, posted at 12:01 am Pacific time (12:31 pm in India).
5. **Through the week:** one helpful post in each community below. Read each community's self-promotion rules first.

## LinkedIn post

> I built the tool I wanted when I started building with AI.
>
> I've designed enterprise software for 11 years. When I started shipping my own apps with Claude and Cursor, the code came fast, but the things I'd normally catch in design review didn't: accessibility, honest competitor research, the "should we even build this?" conversation.
>
> So I made MakerLine, a free, open-source Claude plugin. You type one sentence about your idea and it comes back with:
> → an honest verdict (it told me to pivot one of my own ideas)
> → real competitors, with sources
> → who the idea leaves out, and which accessibility laws apply where you launch
> → wireframes and a draft PRD
>
> It won't write a line of code until you approve the idea. After that it builds one tested task at a time, with WCAG 2.2 AA, security and tests checked at every step.
>
> It's honest about itself too: every mistake it made on real projects is logged publicly, and each one became a fix.
>
> Try it in 5 minutes: https://sairam5294.github.io/makerline/
>
> If you're a designer building with AI, I'd love to know what it gets wrong for you.
>
> #ProductDesign #Accessibility #AI #OpenSource #UXDesign

Alt text for the GIF: "Demo: one sentence about an idea goes in; MakerLine writes the brief, searches competitors, checks India's accessibility and data laws, argues for and against, and writes a one-pager with the verdict Pivot."

## Long article: "What my AI toolkit got wrong"

**Title options:** "What my AI toolkit got wrong (and why I publish it)" · "I asked my own tool if my idea was worth building. It said no."

**Outline (about 1,200 words)**

1. **The problem (150 words).** AI makes building fast and deciding easy to skip. Designers know how to review a product; most can't review code.
2. **What MakerLine does (200 words).** The line: describe → evaluate → see it → you approve → set up → build. The approval gate is enforced by hooks and CI, not by asking nicely.
3. **The ClubSlot story (250 words).** A brief that said "no competitors". The kit found MyGate, NoBrokerHood and ADDA, each with about 25,000 communities, and recommended a booking-only pivot from a WhatsApp link. Screenshot: `2-one-pager.png`.
4. **The RhythmBuddy story (200 words).** A shipped macOS app with 275 passing tests. Four reviewers still found 8 must-fix problems. Screenshot: the review summary.
5. **What it got wrong (250 words).** Pick three rows from `LESSONS.md`. Show the token chart: 157k → 146k → 120k per Quick run, and the target it's still working toward.
6. **Accessible worldwide (100 words).** Why WCAG 2.2 AA is the floor, and why every evaluation asks who the idea leaves out.
7. **Try it, and tell me what breaks (50 words).** The link and the barrier-report route.

## Product Hunt

| Field | Text |
|---|---|
| Name | MakerLine |
| Tagline (60 characters max) | Know if your idea is worth building. Then build it right. |
| Description (260 characters max) | A free, open-source Claude plugin for designers and solo makers. One sentence in: an honest verdict, real competitors, wireframes and a PRD. Nothing is built until you approve; then accessibility, security and tests are checked at every step. |
| Topics | Design Tools · Developer Tools · Artificial Intelligence · Open Source · Accessibility |
| Gallery | 1. `makerline-social-preview.png` · 2. the demo GIF · 3. `2-one-pager.png` · 4. `3-scorecard.png` · 5. `5-wireframes.png` · 6. `6-excluded.png` |
| Pricing | Free |

**Maker's first comment**

> Hi Product Hunt! I'm Sairam, a product designer in Hyderabad. MakerLine is the review process I use at work, packaged so it runs inside Claude for anyone building with AI.
>
> Three things make it different from just asking a chatbot:
> 1. It's willing to say "pivot" or "stop", with a confidence level and the evidence.
> 2. It won't write code until you approve, enforced by hooks and CI.
> 3. Accessibility is the floor, not a feature: WCAG 2.2 AA, plus the accessibility law of wherever you launch.
>
> It's free and MIT-licensed. Everything it writes is plain files in your own folder. I'd love your toughest feedback, especially on what it gets wrong.

## Communities

| Where | Angle | Check first |
|---|---|---|
| r/ClaudeAI | "A plugin that tells you not to build things" + the GIF | Self-promotion rules; post as a project share |
| r/UXDesign | The accessibility and honest-evaluation angle, not the tool | No self-promotion outside allowed threads |
| r/SideProject, r/indiehackers | The ClubSlot pivot story | Fine for project shares |
| Designer communities (ADPList, local UX groups in Hyderabad) | A short talk or demo: "Reviewing AI-built products as a designer" | Ask the organiser |
| Accessibility communities (A11y Slack, a11yproject) | Ask for an expert audit of the kit's rules | Ask, don't pitch |

## First outside testers

Before or right after the LinkedIn post, ask five people to run a Quick pack on their own idea: who to ask, the message to send and the report form are in [`TESTERS.md`](TESTERS.md).

## After each post

- Reply to every comment within a day; turn real problems into GitHub issues.
- Add new users' projects to the showcase when they use the form.
- Note what you learned in `LESSONS.md`.
