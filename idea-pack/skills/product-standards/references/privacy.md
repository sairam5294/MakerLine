# Privacy & Compliance Standard

Not legal advice — a builder's checklist. For launches that handle children's data, health, finance or payments at scale, get a lawyer's review.

## 1. Principles (MUST)

- **Data minimisation**: collect only what a feature needs now; document why each personal-data field exists (data inventory table in `docs/product/PRIVACY.md`).
- **Purpose limitation**: use data only for the purpose stated at collection.
- **Consent & notice**: clear privacy notice in plain language before collection; separate, opt-in consent for marketing and non-essential analytics.
- **User rights**: users can view/export, correct and delete their data and account from inside the app (Apple requires in-app account deletion).
- **Retention**: define how long each data type is kept; delete automatically after that.
- **Security**: see `security.md`; breach response plan with notification timelines.

## 2. Laws to check by audience

| Audience | Law / rule | Key implications |
|---|---|---|
| India | Digital Personal Data Protection Act 2023 + DPDP Rules 2025 (notified Nov 2025, phased: Data Protection Board rules in force now; consent managers 13 Nov 2026; notice, consent, parental consent, security, breach, rights and retention duties **13 May 2027** — build to them now) | Notice + consent, purpose limitation, erasure, breach notification to the Data Protection Board and users, **verifiable parental consent for anyone under 18**, no tracking/behavioural monitoring or targeted ads directed at children |
| EU/UK | GDPR / UK GDPR | Lawful basis, DPA with processors, data residency awareness, cookie consent, children's consent age 13–16 |
| Canada | PIPEDA (federal private sector); provincial laws incl. Ontario **PHIPA** for personal health information (custodians + their vendors), Quebec Law 25 | Consent, breach reporting, health data rules flow to vendors by agreement; residency expectations for health data |
| Australia / Japan | Privacy Act 1988 (APPs) / APPI | Notice, purpose, cross-border transfer rules |
| USA | COPPA (under 13; amended rule effective 23 Jun 2025, compliance required since **22 Apr 2026** — biometric identifiers and government IDs now count as personal information), HIPAA (health data via covered entities and business associates), state privacy laws (CCPA/CPRA etc.) | Verifiable parental consent for under-13s; no behavioural ads to children |
| App stores | Apple App Store Review Guidelines, Google Play Families Policy | Privacy nutrition labels / Data safety form must match reality; Kids category: no third-party analytics/ads without strict compliance, parental gates for links and purchases; age signals (Apple Declared Age Range, Google Play Age Signals) may be used only for age compliance — never ads, profiling or analytics |

*Dates last verified 2026-10-20.*

## 3. Children's products (extra MUST)

- Parent account owns the child profile; child never enters email/phone.
- Parental gate before external links, purchases, settings and sharing.
- No third-party advertising or behavioural tracking; analytics only first-party, aggregated or child-safe SDKs.
- No open chat or user-generated content visible to other children unless heavily moderated.
- Minimal data: nickname + age band, not full name/birthdate/photo.

## 4. Analytics

- Prefer privacy-friendly analytics (PostHog with IP anonymisation, Plausible, Firebase with ad-ID collection disabled).
- Never send personal data (emails, names, free text) as analytics event properties.
- Honour opt-out; on iOS request App Tracking Transparency only if you actually track across apps (usually you shouldn't).

## 5. Payments

- Use a payment provider (Razorpay, Stripe, App Store / Play Billing for digital goods inside apps); never store card data.
- Digital content/subscriptions consumed in-app must generally use Apple/Google in-app purchase — check current store rules and regional exceptions before designing monetization.

## 6. Required documents before launch

- Privacy policy, terms of service, data inventory, store privacy labels, cookie notice (web), grievance/contact officer details where required (India DPDP).
