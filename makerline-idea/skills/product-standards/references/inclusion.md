# Inclusion & Non-discrimination Standard

Owner decision (16 Oct 2026): **every product is accessible worldwide and discriminates against no one, whatever its first launch market.** Launch-market law (`accessibility-law.md`) decides what you must *prove* and *publish*. This file decides what you *build*, and it applies everywhere.

## 1. Global accessibility baseline (MUST, every product)
- WCAG 2.2 AA (`accessibility.md`). This meets or exceeds the WCAG level most accessibility laws cite; check `accessibility-law.md` for the exceptions.
- The non-WCAG items that laws such as the European Accessibility Act, AODA and Section 508 add: an accessibility statement, a barrier-feedback route with a reply time, information in alternate formats on request, accessible support channels (not phone-only), accessible documents (tagged PDFs or HTML), captions and transcripts.
- Keep evidence as you go (test notes, audit results) so an Accessibility Conformance Report (VPAT) can be written in a day when a buyer asks.

## 2. Age
- Older adults: text scaling without breaking, high contrast, generous targets, no time pressure, no puzzle CAPTCHAs, simple sign-in (passkeys, magic links), undo for destructive actions, a human help route.
- Children: follow `privacy.md` (parental consent, minimum data), and design for their reading level.

## 3. Language, literacy and culture
- Plain language by default (aim for a reading age of about 12); one term per concept; icons always paired with text.
- Support the scripts and languages of the audience; translations by native speakers, never machine-only for critical text. Mark language changes in content. Support right-to-left layouts if Arabic, Urdu or Hebrew are in scope.
- Localise dates, times, numbers, currencies and calendars; never assume one time zone.
- Imagery and examples reflect the real audience (age, skin tone, body, disability, family types) without stereotypes. Check colour and symbol meanings for each culture.

## 4. Names, identity and personal data
- One free-text "Full name" field (plus an optional "What should we call you?"). Accept any characters, length and order; no first/last name split unless a legal or payment system requires it.
- Don't ask for gender, title, religion, caste, ethnicity, marital status or date of birth unless the product genuinely needs it. If you must ask: make it optional, explain why, offer "prefer not to say" and a self-describe option. Pronouns are optional.
- Phone numbers: international format with a country picker. Addresses: free-form fields that work outside one country.
- Household and family models fit real lives (single parents, extended families, carers, same-sex couples).

## 5. Device, network and cost
- Works on low-end Android phones, older OS versions (state the minimum), slow or intermittent networks, and limited storage. Measure on a low-end device (`performance.md`).
- Core tasks don't depend on the newest phone, a fast connection or a camera. Offer a fallback (web link, SMS, email) where it matters.
- Pricing and payment don't shut people out: a free or low-cost path where possible, local payment methods, no surprise data-heavy downloads.

## 6. Fair decisions
- Never set prices, eligibility, ranking or visibility based on protected characteristics (disability, age, gender, religion, caste, ethnicity, sexual orientation) or close proxies (postcode, name, language) without a lawful, explained reason.
- AI features: include fairness cases across groups and languages in the eval set (`ai.md`); users can appeal to a human and get an explanation.
- Moderation and reporting tools protect people from harassment and are accessible themselves.

## 7. Research and testing
- Recruit across ability, age, language, device and income. Include assistive-technology users in every prototype round (`idea-pack/references/accessibility-user-testing.md`). Pay everyone fairly.
- Ask what tools and strategies people use, never for diagnoses.

## Checks (design-direction, design-qa, quality-review)
1. Who can't complete the core task, and why? (persona spectrum: permanent, temporary, situational)
2. Any required field that excludes someone (name format, gender, phone, address, ID)?
3. Does it work at 200% text, on a low-end phone over a slow network, and in each launch language?
4. Is any decision or price based on a protected characteristic or a proxy?
5. Is the accessibility statement and feedback route in place, and is ACR evidence kept?
