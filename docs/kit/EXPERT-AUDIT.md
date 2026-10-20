# Expert screen-reader audit: brief and shortlist

Automated checks (axe) find 0 issues on every page of the site, but they catch only about a third to half of real problems. An expert audit with real assistive technology, ideally including testers who use it every day, is the next level of proof. This page is ready to send; **booking it is Sairam's decision, because it costs money.**

_Researched 2026-10-21. Prices are what the providers' pages said on that date; ask for a quote before deciding._

## Scope to send

**What to test (about 10 screens):**

1. Docs site home page (English) and the Hindi home page
2. "Start in 5 minutes" guide (long page with the contents panel and copy buttons)
3. Overview page (long page, tables)
4. Case study page and the ClubSlot one-pager
5. Wireframes the kit generates (`example/wireframes/`, prototype mode)
6. The local cockpit (`scripts/kit-ui.py`), the kit's own web interface
7. The Expo starter app on iPhone and Android (home and sign-in screens)
8. The web starter's landing page and waitlist form

**Assistive technology:** VoiceOver on macOS (Safari) and iOS, NVDA on Windows (Chrome or Firefox), TalkBack on Android, plus keyboard only, 200% and 400% zoom, and Windows High Contrast (forced colours).

**Standard:** WCAG 2.2 AA, plus EN 301 549 clause 11.7 (user preferences) for the apps.

**Deliverables:** an issue list mapped to WCAG success criteria, with severity, steps to reproduce and the assistive technology used; short screen recordings of blocking issues; a re-test of fixes. A conformance report (ACR/VPAT) is optional.

## Shortlist

| Provider | What they offer | Price | Why consider |
|---|---|---|---|
| [BarrierBreak](https://www.barrierbreak.com/web-accessibility-testing/) (India, US, Singapore) | Manual WCAG testing with native screen readers; testers with disabilities; empanelled auditor with India's DEPwD | Quote after a 30-minute call (sales@barrierbreak.com) | Based in India, with lived-experience testers; knows RPwD and GIGW |
| [Fable](https://makeitfable.com/pricing) | Testing by people with disabilities (screen reader, magnification, alternative navigation): videos, transcripts, usability score | Pay-per-project, price shown after creating a free account; up to 3 testers, from 5 days | Real users' experience, not only a checklist; good for the site and the starters |
| [Accessible.org](https://accessible.org/pricing/) | WCAG audit by sampled pages, screen reader testing with NVDA, JAWS or VoiceOver | $100–250 per main page, $25–100 per light page; most audits $1,250–2,750; iOS testing extra | Published prices; a clear scope for a small site |

**Suggested first step:** ask BarrierBreak and Fable for quotes on the scope above, and compare them with Accessible.org's published range. One option is a Fable pay-per-project round on the site and starters first (real users), then a checklist audit only if that round finds structural problems.

## Request email

> Subject: Quote request: accessibility audit of an open-source product toolkit
>
> Hello, I maintain MakerLine, a free, open-source Claude plugin with a docs website, generated wireframes, a small local web app and two starter apps (Expo for iOS/Android, Next.js for web). We target WCAG 2.2 AA and run automated axe checks, and we'd now like an expert audit with screen readers (VoiceOver, NVDA, TalkBack), keyboard-only and zoom, ideally including testers who use assistive technology daily. The scope is about 10 screens (list attached). Could you share a quote, timeline and sample report? Site: https://sairam5294.github.io/makerline/ · Repo: https://github.com/sairam5294/makerline. Thank you, Sairam Mogullapalli

## After the audit

Turn every finding into an accessibility issue, fix the blocking ones first, re-test, and update the accessibility statement's "Known limitations" and "Last checked" date.
