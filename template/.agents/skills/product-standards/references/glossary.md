# Glossary

Purpose: one plain-language line for each term the kit's rules use, so the owner and any AI tool read them the same way.

## Accessibility

| Term | Plain meaning |
|---|---|
| **Accessible name** | The text a screen reader or speech-input tool uses for a control, e.g. "Save" for a save button. Usually the visible label; must contain it. |
| **ACR / VPAT** | VPAT is ITI's blank template; an Accessibility Conformance Report (ACR) is the filled-in report that tells buyers how well a product meets WCAG, Section 508 or EN 301 549. How-to: `acr-vpat.md`. |
| **ACT rules** | W3C's Accessibility Conformance Testing rules: precise test recipes so tools and people check a WCAG criterion the same way. axe-core implements many. |
| **AODA / IASR** | Ontario's Accessibility for Ontarians with Disabilities Act and its main regulation, the Integrated Accessibility Standards (O. Reg. 191/11): customer-service, information, web and training duties. See `accessibility-law.md`. |
| **APG** | W3C's ARIA Authoring Practices Guide: the reference patterns (roles, states, keyboard keys) for custom widgets like tabs, menus and dialogs. |
| **EN 301 549** | The European accessibility standard for all ICT (web, software, hardware, documents, support). Includes WCAG plus extra clauses; used by the EU Accessibility Act and public buyers. |
| **Focus trap** | Keeping keyboard focus inside an open dialog until it closes — wanted in modals. An *unwanted* trap (you can't tab out at all) is a WCAG failure. |
| **Landmark** | A labelled region of a page (header, nav, main, footer, search) that screen-reader users jump between. Use `<header>`, `<nav>`, `<main>`, `<footer>`. |
| **Live region** | Part of the page that screen readers announce when it changes, without moving focus — used for "Saved", errors, chat replies (`aria-live="polite"`, `role="status"`). |
| **Roving tabindex** | A way to give a group of items (tabs, toolbar, menu) one Tab stop: the active item has `tabindex="0"`, the others `-1`, and arrow keys move between them. |
| **WCAG-EM** | W3C's method for evaluating a whole website or app: set scope, explore, pick a sample of screens, audit, report. |

## Engineering

| Term | Plain meaning |
|---|---|
| **RLS (Row-Level Security)** | A database rule (e.g. in Supabase/Postgres) that lets each user read or change only their own rows, enforced by the database even if the app code has a bug. |
