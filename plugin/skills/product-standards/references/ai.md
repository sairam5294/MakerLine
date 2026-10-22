# AI Features Standard

For any product feature that uses an AI model: chat, generation (text, image, audio, music, voice), summaries, recommendations, classification, search, agents. Security of AI features is also covered in `security.md` §5.

## 1. Should this be AI at all? (MUST answer in the PRD)
- What user problem does it solve, and what's the non-AI alternative (rules, search, templates, a human)? Choose AI only if it is clearly better for users, not because it's trendy.
- What happens when the AI is wrong? If a wrong answer can cause harm (health, money, legal, children, safety), design for human review or don't ship it.
- Can users do the core task without the AI? (MUST for core flows: AI outages happen.)

## 2. Model & architecture
Starting point: the web starter's `src/ai/` harness (provider wrapper, versioned prompt, schema, redaction, quota, live eval runner).
- Call models **only from the server** (edge/server function); keys never reach the client.
- Pick the cheapest model that passes your evals (§4); record model + version in TECH_STACK.md. Re-run evals before switching models.
- Current families (verified 2026-10-20 in provider docs — re-check before recording): Anthropic Claude Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5; OpenAI GPT-6 Astra / GPT-6.1 Sol / GPT-6 Luna; Google Gemini 4 Argon, Gemini 3.8 Flash, Gemini 3.5 Flash-Lite. Start with the fastest tier (Haiku, Luna, Flash-Lite) and move up only when evals fail.
- Keep prompts in version-controlled files (`src/ai/prompts/<feature>.v1.md`), not inline strings; change = new version + eval run.
- Ask for **structured output** (JSON schema) and validate it with Zod before use; on invalid output retry once, then fall back.
- Set timeouts (≤ 30 s), retries with backoff, and a graceful fallback message.

## 3. UX for AI (MUST)
| Need | Pattern |
|---|---|
| Waiting | Stream tokens or show step progress; never a frozen screen. Allow cancel. |
| Transparency | Label AI-generated content ("Written with AI"); say what it can't do. |
| Control | Users can edit, regenerate, undo, or turn the feature off. AI never takes an irreversible action without confirmation. |
| Errors | Plain-language failure + retry + non-AI path. Don't blame the user. |
| Trust | Show sources/citations for factual answers; say "I'm not sure" rather than invent. |
| Feedback | 👍/👎 + "report a problem" on outputs (also required by Google Play for generative-AI apps). |
| Accessibility | Chat: announce each **finished** message (or a short "Assistant is replying" then the result) in a polite live region — never every token. A visible **Stop** button reachable by keyboard and screen reader while generating. Keep focus in the message box after sending; don't steal focus when the reply lands; new messages added below, history in a list with headings or labels per speaker. AI-written alt text is a draft: a human checks it before publishing. Voice features need text alternatives. |
| Onboarding | Set expectations with 2–3 example prompts; show limits (daily quota) before users hit them. |

## 4. Quality: evals before launch (MUST)
- Build a small eval set per feature (`evals/ai/<feature>.cases.json`, scored by the web starter's AI eval script): 20–50 real-looking inputs incl. edge cases, other languages (Telugu/Hindi if relevant), empty/abusive inputs, and prompt-injection attempts.
- Define pass criteria (correct, safe, on-format, tone) and score every prompt/model change against the set; store results in `docs/product/ai-evals/`.
- Track in production: error rate, fallback rate, 👎 rate, cost per active user, latency p95.

## 5. Safety & abuse
- Treat user input AND retrieved content (web pages, documents) as untrusted: defend against prompt injection; the model never gets tools or data beyond what the feature needs.
- Moderate inputs and outputs for harmful content (provider moderation endpoints or classifiers). Stricter settings for children (no open-ended chat; curated, pre-generated or tightly constrained outputs; parent visibility).
- Rate-limit per user and per IP; cap tokens per request and per user per day.
- Never let the model's output decide authorization, prices or payments.

## 6. Privacy & data (MUST)
- Tell users what is sent to the AI provider; get consent where personal data is involved (DPDP/GDPR). Minimise: strip names, emails, phone numbers before sending when possible.
- Choose providers/settings that don't train on your API data; record the provider as a processor in the data inventory (`privacy.md`).
- Don't log full prompts containing personal data; log IDs + metrics.
- Children: no personal data to AI providers without verifiable parental consent; prefer on-device or pre-generated content.

## 7. AI-generated content & rights
- **Know your rights to outputs**: check each generator's terms (commercial use, ownership, attribution). Some music/image tools grant commercial *use* but not *ownership*; AI-only output may not be copyrightable, so competitors could copy it. For content that is your product's core value (songs, stories, art), prefer human-created or human-edited work you own, or licensed libraries.
- **Never** generate imitations of real artists' voices/styles, real people, logos, or copyrighted characters/songs; don't train or prompt on content you don't have rights to.
- **Label synthetic media**: India's IT Amendment Rules 2026 (in force 20 Feb 2026) require clear visible labels for AI-generated images/video, audible disclosure for audio, and embedded metadata/identifiers where feasible for platforms that let users create such content, plus fast takedown timelines. Label AI content in-app regardless — it builds trust.
- **EU AI Act (Article 50, applies from 2 Aug 2026)** to any app offered in the EU: tell users when they are talking to an AI (unless obvious); providers mark AI-generated audio/image/video/text in a machine-readable way (systems already on the market before 2 Aug 2026 have until 2 Dec 2026); disclose deepfakes and AI-written public-interest text. The Digital Omnibus moved Annex III high-risk duties to 2 Dec 2027 (approved June 2026; Official Journal publication unverified). Verified 2026-10-20.
- **Store rules**: Google Play's AI-Generated Content policy applies to apps whose core feature is generative AI (chatbots, image/voice generators): prevent harmful outputs and provide in-app reporting/flagging. Apple requires the same safety and privacy standards plus accurate privacy labels; since 16 Oct 2026 Guideline 1.2 explicitly bans nonconsensual intimate imagery (incl. AI-generated) and "nudification" apps — generators must proactively prevent and remove it.
- Keep a record of how each piece of content was made (tool, prompt, human edits, date) in `docs/product/CONTENT_SOURCES.md`.

## 8. Cost
- Estimate cost per active user per month before building (tokens × price × uses); put it in the unit economics.
- Cache repeated results; pre-generate content that doesn't need to be live; batch non-urgent jobs.
- Free tiers get quotas; show remaining quota in the UI. Billing alerts on the provider account.

## 9. Local / on-device models
- Consider local models (e.g. Ollama on your Mac for development tasks, on-device models in apps) for privacy-sensitive or offline features — test quality with the same eval set; they are usually weaker than cloud models.
