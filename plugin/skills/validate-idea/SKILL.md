---
name: validate-idea
description: Tests demand before building — kill criteria, landing page + waitlist, user interviews, prototype usability test — and records results in VALIDATION.md. Use after evaluation or for "validate demand", "test before building", "interview users".
---

# Validate Idea

Goal: evidence that real people want this, for the least time and money.

1. From EVALUATION.md pick the 1–3 riskiest assumptions. For each, set a **kill criterion** before testing (e.g. "< 40 waitlist signups from 1,000 visitors in 14 days → rethink"). Record them in `docs/product/VALIDATION.md` (template: `references/validation-template.md`).
2. Choose tests (cheapest first):
   - **Interviews** (5–10): use `references/interview-guide.md`. Ask about past behaviour, never "would you use…?".
   - **Landing page + waitlist**: one-page promise, 3 benefits, one CTA, privacy note; track visits → signups. Build it as a **separate project** (`new-project.sh ~/Projects/<name>-landing --web`; owner approves it with `scripts/approve.sh "validation landing page"`), or as static files in this project's `validation/` folder — both pass the approval gate. Deploy on Vercel.
   - **Prototype test** (5 users): the design-direction wireframes in Prototype mode (`design/wireframes/index.html`) or a Figma prototype, 3 tasks, measure task success + time + confusion points. Include 1–2 assistive-tech users if your audience needs it (`../test-plan/references/accessibility-user-testing.md`).
   - **Concierge/manual MVP**: deliver the value by hand (WhatsApp, Google Sheet) to 5–10 users for 2 weeks.
   - **Pre-sale / deposit** when money is part of the model.
3. Run, then record raw results, compare with kill criteria, and summarise: validated / invalidated / unclear + what changes.
4. Feed results into evaluate-idea (re-score with new evidence) before the approval gate.
