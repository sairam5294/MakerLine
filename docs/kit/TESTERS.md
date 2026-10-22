# First five outside testers

The most useful test left is five people who aren't Sairam running a Quick Idea Pack on their own idea and saying what happened. This page is the kit for that: who to ask, what to send them, and how their reports come back.

## Who to ask

Aim for five different people, because one kind of user hides the others' problems:

| # | Who | Why |
|---|---|---|
| 1 | A product or UX designer who has never used Claude Code | The main audience; tests the install and the wording |
| 2 | A solo maker or indie developer | Tests whether the verdict and competitors feel real |
| 3 | A product manager | Tests the PRD and one-pager against what PMs expect |
| 4 | A screen reader or keyboard-only user | Tests the site, the plugin's outputs and the wireframes for real access |
| 5 | Someone outside India, or writing in another language | Tests the accessibility-law section and non-English prompts |

Good places to find them: your LinkedIn post (`LAUNCH.md`), ADPList mentees and mentors, local UX groups in Hyderabad, and an accessibility community (ask, don't pitch).

## Message to send

> Hi {name}, I've built a free, open-source Claude plugin called MakerLine. It takes a few sentences about a product idea and gives back an honest verdict, real competitors and a one-page summary. Would you try it on an idea of yours and tell me what worked and what didn't? It takes about 10 minutes plus a few minutes of waiting. Here's the 5-minute guide: https://sairam5294.github.io/makerline/five-minutes.html. When you're done, the report form is here: https://github.com/sairam5294/makerline/issues/new?template=quick_run_report.yml (or just reply to this message). Thank you!

## What testers do

1. Install MakerLine or MakerLine Idea (the 5-minute guide, step 1).
2. Connect an empty folder and run `/makerline-idea:start give me everything for this idea, quick: …` with their own idea.
3. Read `docs/product/ONE_PAGER.md`.
4. Fill in the report form, or reply to the message with the same answers.

## How reports come back

- **GitHub form:** "Quick run report" (`.github/ISSUE_TEMPLATE/quick_run_report.yml`). It asks only what's needed, and every question except the first is optional.
- **No GitHub account:** testers reply to your message. Copy their answers into the same form so all reports live in one place.
- **Privacy:** testers should never paste a confidential idea. The form says this, and a summary of the idea is enough.

## What to do with the reports

| After | Do |
|---|---|
| Each report | Label it, thank the tester, and turn anything broken into its own issue |
| Five reports | Add a row to `LESSONS.md` per problem found; fix the top three; note the results in `evals/results.md` |
| Testers who agree | Add their project to the showcase (`showcase.yml` form) |
