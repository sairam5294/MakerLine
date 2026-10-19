# Product Kit

<p class="lead">An open-source Claude plugin that takes a product idea from "I have a new idea" to a shipped web, iOS or Android product, with accessibility, UX, security and testing standards built in and enforced.</p>

**Who it's for:** designers and solo makers who build with AI and have light coding skills. It was built by one: a UX designer who wanted every AI tool he used to start thinking like a senior product designer, every session, without being reminded.

[Try it in 5 minutes](five-minutes.md) · [See real runs](case-studies.md) · [Getting started](../../GETTING-STARTED.md)

## What you get

<div class="cards" markdown="1">
<section markdown="1">
### An honest answer before any code

The **Idea Pack** turns a few sentences into a brief, a researched evaluation with a verdict (Go, Go with changes, Pivot or Drop), real competitors with a differentiator test, the strongest version of the idea and a path to Go.
</section>
<section markdown="1">
### Something you can show people

A design direction with clickable low-fi wireframes, a draft PRD and a one-page summary, all in plain Markdown and HTML files in your own folder.
</section>
<section markdown="1">
### Rules that are enforced, not just written

After **you** approve the idea: brand, stack, design system, engineering docs, build, review, test and ship, with WCAG 2.2 AA, OWASP 2025 and test rules checked by hooks, git hooks and CI. No AI tool can approve the idea for you.
</section>
</div>

Accessible worldwide is the baseline: every evaluation asks who the idea leaves out and which accessibility laws apply where you launch (for example AODA, ADA, the European Accessibility Act and India's RPwD Act).

## Try it

Connect an empty folder to a new chat, then type one of these:

- *"/product-kit:start — Give me everything for this idea, quick: a booking app for small physio clinics"*
- *"I have a new idea: …"* (a short interview, one round at a time)
- *"Who are my competitors and what's my real differentiator?"*
- *"What would it look like?"* (design direction and clickable wireframes)
- *"Make my tool plan — I have Claude, ChatGPT and Cursor"*

Using the Idea Pack plugin instead? Start with `/idea-pack:start` in place of `/product-kit:start`.

## Install

### Claude app (desktop or web)

1. Open **Customize** in the left sidebar, then **Plugins**.
2. Choose **Add marketplace** and enter `sairam5294/product-kit`.
3. Find **idea-pack** or **product-kit** in the list and choose **Install**.
4. For updates, turn on **Sync automatically** for that marketplace.

### Claude Code

```bash
claude plugin marketplace add sairam5294/product-kit
claude plugin install idea-pack@product-kit-marketplace      # or: product-kit@product-kit-marketplace
```

Check it worked: start a new chat and type `/idea-pack:` or `/product-kit:`. The list of skills should appear.

## Idea Pack or the full kit?

Install one, not both: the full kit already contains the Idea Pack, and every skill would appear twice.

| | Idea Pack | Full Product Kit |
|---|---|---|
| Best for | Deciding whether an idea is worth building | Building and shipping it once you've decided |
| What it does | Discovery, evaluation, competitors, design direction with wireframes, draft PRD, one-pager, validation tests, tool plan | Everything in the Idea Pack, plus naming and brand, tech stack, design system, full PRD, engineering docs, repo setup, build, review, test, ship and post-launch |
| Writes code? | No, only documents and HTML wireframes | Yes, after you approve the evaluation |
| Needs a terminal? | No | Only for building (Claude Code, Cursor or Codex) |
| Start with | `/idea-pack:start` | `/product-kit:start` |
| Read more | [Idea Pack](../../idea-pack/README.md) | [Full overview](../../README.md) |

<div class="note" markdown="1">
**Not sure?** Start with the Idea Pack. If you decide to build, remove it and install the full kit: your documents stay in your folder, and `/product-kit:start` reads their status and offers the next step.
</div>

## See it on real projects

- [RhythmBuddy](case-rhythmbuddy.md): a shipped macOS app adopted into the kit, then reviewed. Four reviewers found 8 must-fix problems in a project that already had 275 passing tests.
- [ClubSlot](case-clubslot.md): an Idea Pack run on a brief that claimed "no competitors". The kit found the real ones and recommended a sharper pivot.

## Open source, and honest about its mistakes

MIT licence. Every project's mistakes are logged in [What the kit got wrong](../../LESSONS.md) and turned into fixes listed in the [changelog](../../CHANGELOG.md). Found a bug, an outdated rule or an accessibility barrier? [Open an issue](https://github.com/sairam5294/product-kit/issues/new/choose).

Created by **[Sairam Mogullapalli](https://github.com/sairam5294)**, UX designer, building products with AI.
