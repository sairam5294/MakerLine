# Case study: ClubSlot

What the Idea Pack does with a confident brief: amenity booking for gated communities, pitched as having "no competitors".

## The run

| Fact | Detail |
|---|---|
| The idea, as briefed | Android and iOS apps plus a web admin for gated communities in Hyderabad: amenity booking, UPI payments, notices, visitor passes and complaints, in 10 weeks at 10 hours a week |
| Kit version and depth | v0.8.0, Standard depth, run on 19 October 2026 |
| How it was run | Blind: an agent followed the skills from the brief in the kit's evals and never saw the answer key. The owner was treated as unavailable, so every decision is a marked default for the owner to confirm |
| Research used | 12 web searches and 8 page reads, inside the Standard budget |
| Checked by | `check_idea_pack.py`: 0 failures, 0 warnings |

## What the brief claimed, and what the research found

The brief said there were no competitors. The evaluation found at least ten Indian society-management products that already bundle amenity booking. The two leaders, MyGate and NoBrokerHood, each claim around 25,000 or more communities, and so does ADDA (all vendor figures, cited in the files).

The gap was not the feature. It was the experience and the segment: the leaders are ad-funded, notification-heavy super-apps built around the security gate, and many mid-size communities still book through WhatsApp and a paper register.

## The verdict: Pivot

The idea **as briefed** scored 4.95 out of 10. Two problems drove the score down: the scope was not buildable for one person working 10 hours a week, and the "no competitors" positioning was wrong.

The kit did not stop at "no". It wrote the **strongest version** of the idea and scored that too, reaching a target of 6.40 out of 10:

> A booking-only, fair-rules, no-install web service for mid-size Hyderabad communities still on WhatsApp and paper. Residents book from a link pinned in the community WhatsApp group, the committee's rules are enforced visibly by the system, and the guard reads a desk view in five seconds.

Confidence was rated **Medium-Low**, because the evidence was mostly vendor claims and no interviews had happened yet. The evaluation says so plainly.

## What the Idea Pack produced

- **A one-pager** with the verdict, the six defaults to confirm, the reality check and the next test
- **An evaluation** with a scorecard, every score's evidence and a "raise it by…" step for each weak dimension
- **A competitor analysis** with a differentiator test, including review complaints about the leaders where they could be found, and "Unknown" where they couldn't
- **A design direction** with eight clickable, contrast-checked wireframe screens for phone, tablet and desktop
- **A draft PRD** for the pivot, with 9 must-have stories and an estimate of about 8 weeks at 10 hours a week
- **A clarity log**: 11 open questions, 6 of them blocking, each with the decision it blocks

## Accessibility and inclusion, from the first document

The evaluation asked who the idea could leave out, before any design. Its answers shaped version 1:

- Older residents and people with low vision: text that scales to 200%, 4.5:1 contrast, one amenity per screen
- Telugu-first readers, including guards and staff: English and Telugu from version 1, icons always with text
- Screen-reader users: every slot is a real button with its name, time and state; availability is never shown by colour alone
- People without a smartphone: the desk can book on a resident's behalf

It also listed obligations by launch market (India's RPwD Act, the DPDP Act for personal data, and payment rules) and found no published accessibility statement for any of the three leaders: a gap ClubSlot could fill. The section is labelled "Not legal advice".

## The next step it recommended

Not code. Five conversations with community committees, using a price card and the clickable wireframes. The test has clear rules set in advance: **go** if at least 3 of 5 would run a pilot and at least 2 accept ₹8 per flat or ₹1,500 per month; **rethink** if none would pay anything.

## What the kit got wrong on this run

The agent logged 15 places where the kit's own instructions were unclear or contradictory, on top of 29 from an earlier run on the same brief. Examples: two different word limits for the one-pager, no tablet size in the wireframe template, and a store-rating lookup that used up the reading budget. All were fixed in kit version 0.8.0. The full list is in the example's friction log.

## Read the actual files

- [The full ClubSlot Idea Pack](../../examples/idea-pack-clubslot/README.md), starting with the one-pager
- [The clickable wireframes](../../examples/idea-pack-clubslot/design/wireframes/index.html)
- [The friction log on GitHub](../../examples/idea-pack-clubslot/KIT_FRICTION.md)

Prices, ratings and review quotes in the files were checked on the dates shown and will go stale.

[Back to case studies](case-studies.md)
