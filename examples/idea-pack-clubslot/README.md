# Example Idea Pack — "ClubSlot" (blind eval run, 19 Oct 2026, kit v0.8.0, Standard depth)

Produced by an agent following the kit's skills blind (it never saw the answer key) from the brief in `evals/cases/community-amenities`. The owner was treated as unavailable, so decisions are defaults marked for confirmation.

Start with [`docs/product/ONE_PAGER.md`](docs/product/ONE_PAGER.md), then [`docs/product/README.md`](docs/product/README.md) for the index. Wireframes: open `design/wireframes/index.html` in a browser (add `?mode=prototype` to click through).

What it shows: a brief claiming "no competitors" gets a researched Pivot verdict (MyGate, NoBrokerHood, ADDA, ApnaComplex), the strongest version worth testing (booking-only, fair rules, no-install web app from a WhatsApp link), a path to Go, an accessibility-and-compliance section (RPwD/GIGW, DPDP, who is excluded), design direction with 8 contrast-checked wireframes (phone, tablet and desktop), and a draft PRD for the pivot. Produced with 12 searches and 8 page reads inside the Standard budget; `check_idea_pack.py` passed with 0 fail, 0 warn. `KIT_FRICTION.md` is the agent's own log of where the kit's instructions were unclear (fixed in 0.8.0).

Prices, ratings and review quotes were checked on the dates shown in the files and will go stale.

## What the kit got wrong on this run
The 16 Oct run logged 29 friction points (fixed in 0.7.0); this 19 Oct run logged 15 more (fixed in 0.8.0): no owner-unavailable mode, Drop/Pivot rules overlapped, no rule on whether to design the brief or the pivot, US App Store ratings for an India product, non-button option chips in the wireframe template. See `LESSONS.md`.
