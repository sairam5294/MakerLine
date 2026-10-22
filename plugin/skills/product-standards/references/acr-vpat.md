# ACR / VPAT — a short how-to

Purpose: write an honest Accessibility Conformance Report (ACR) when a business, school or government buyer asks for one. A **VPAT** is the blank template from ITI; an **ACR** is the filled-in report.

## 1. Pick the edition

Current template: **VPAT 2.5Rev** (ITI, April 2025). Use the edition your buyer names; if unsure, ask.

| Edition | Covers | Use when selling to |
|---|---|---|
| **WCAG** | WCAG 2.2 (A, AA, AAA tables) | Most private buyers; the default |
| **508** | Revised Section 508 (WCAG 2.0 AA + software, hardware, docs and support) | US federal agencies; many US states and universities |
| **EU** | EN 301 549 (WCAG 2.1 AA + non-web clauses) | EU public sector; EAA-covered customers |
| **INT** | All three in one report | Buyers in several markets |

## 2. Fill it from testing, not memory

- Base every row on a real evaluation of the product version you name — automated scan **plus** manual keyboard, screen-reader, zoom and speech-input passes (`../../product-standards/references/accessibility.md` §6). ITI's own guidance: test against each section, then record the results.
- Fill the header: product name and version, report date, contact, and **evaluation methods used** (tools, assistive tech + browser combinations, who tested).
- Use only these conformance terms:

| Term | Means |
|---|---|
| **Supports** | Meets the criterion with no known defects (or meets it through an equivalent accessible alternative) |
| **Partially Supports** | Some functionality does not meet the criterion |
| **Does Not Support** | Most functionality does not meet the criterion |
| **Not Applicable** | The criterion is not relevant to the product (say why) |
| **Not Evaluated** | Only allowed for WCAG Level AAA rows |

- The **Remarks** column explains every "Partially" or "Does Not Support": what fails, where, and the planned fix date. Vague remarks ("mostly accessible") lose deals and trust.

## 3. Rules

- Never mark "Supports" for something you didn't test. An overstated ACR becomes a contract and a legal risk.
- Date it; re-test and re-issue for every major release (or at least yearly).
- Keep the test evidence (scan reports, screen-reader notes) next to the ACR in `docs/product/` — buyers and auditors ask for it.
- Link the ACR from the accessibility statement.

_Source: ITI VPAT page (itic.org/policy/accessibility/vpat), accessed 2026-10-20. "Not Evaluated" limited to Level AAA re-checked 2026-10-21 against ITI's VPAT 2.5 instructions._
