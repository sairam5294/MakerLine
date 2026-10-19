# Figma wireframes

How `design-direction` mirrors the HTML wireframes into a Figma file when the Figma connector is available, and what to offer when it isn't.

## Ground rules

- **HTML is the source of truth.** Build `design/wireframes/index.html` first and pass `check_idea_pack.py`; Figma mirrors it. If the two differ, fix Figma, not the HTML.
- **Owner's say-so first.** Ask once: *"Build these in Figma too — a new file, or paste a file URL?"* A pasted URL means: parse the `fileKey` from `figma.com/design/:fileKey/…` and add pages there.
- **Load the Figma skills before the calls they guard:** `figma-create-new-file` before `create_new_file`, `figma-use` (and `figma-generate-design`) before `use_figma`, `figma-generate-diagram` before `generate_diagram`. If those skills aren't installed, the server serves them as `skill://figma/<name>/SKILL.md`.
- **Never invent tool names.** If a client exposes different names, use its create-file / write / screenshot tools for the same steps.

## Confirmed tools

Checked 2026-10-20 against Figma's [Tools and prompts](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/) page.

| Tool | Use in this skill | Notes |
|---|---|---|
| `whoami` | check the plan and seat before writing | remote only |
| `create_new_file` | new blank Design file (or FigJam for flows) | remote only; asks which plan if the owner has several |
| `use_figma` | create pages, styles, components, frames, prototype links (Plugin API JavaScript) | remote only; the main write tool |
| `get_screenshot` | look at each frame after building it | one node per call, PNG; counts as a read |
| `get_metadata` | light XML outline to check page and frame names | counts as a read; cheaper than `get_design_context` |
| `generate_diagram` | FigJam flow diagram from the Mermaid in §5 | remote only |
| `search_design_system` | only if the owner names a wireframe kit or library to reuse | remote only; low-fi usually needs none |
| `html_to_figma` | optional fast start: convert the self-contained HTML into layers, then tidy with `use_figma` | documented; not every client exposes it |
| `generate_figma_design` | captures a live web UI — not needed for wireframes | select clients only |

## Access, cost and limits

| Topic | What Figma says | What to do |
|---|---|---|
| Server | remote server at `https://mcp.figma.com/mcp`; all write tools are remote only | the desktop server can't build these |
| Seat | a **Full seat** is needed to write outside your drafts | on Starter / View / Collab, the file lands in the owner's drafts — say so |
| Cost | writing to the canvas is free in beta and *"will eventually become a usage-based paid feature"* | mention once; never start paid usage without asking |
| Rate limits | reads count: View/Collab seats and Starter 20 calls a month; Professional Full/Dev 200 a day; write tools such as `create_new_file` are exempt | on 20/month, screenshot a whole Section per 3–4 frames instead of each frame, and skip `get_metadata` until the end |

Sources: [Figma MCP server overview](https://developers.figma.com/docs/figma-mcp-server/), [Rate limits & access](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/). Limits change; re-check in `standards-refresh`.

## File structure

- **File name:** `<Product> — Wireframes v<n>` (`n` matches the DESIGN_DIRECTION draft). FigJam flows, if used: `<Product> — Flows v<n>`.
- **One page per platform in scope**, named after it; add a `Notes` page only if the owner wants a cover.

| Page | Frame size | Matches HTML `data-device` |
|---|---|---|
| Phone | 390 × 844 | `phone` (HTML frame 360 wide) |
| Tablet | 834 × 1194 | `tablet` (HTML frame 768 wide) |
| Desktop | 1440 × 1024 | `desktop` (HTML frame 1024 wide) |

The HTML frames are narrower so they fit a browser; Figma uses standard device sizes. Same content and order — only the width changes.

## Foundations (one `use_figma` call)

- **Colour styles** copied from the HTML template's `:root`, prefixed `wf/`. Text pairs are all ≥ 4.5:1:

| Style | Hex | Used for | Contrast on `wf/paper` · `wf/fill` |
|---|---|---|---|
| `wf/ink` | `#1d1d1f` | text, primary button fill | 16.8 · 14.5 |
| `wf/muted` | `#5f6368` | secondary text | 6.1 · 5.2 |
| `wf/danger` | `#a50e0e` | error text and borders | 7.9 · 6.8 |
| `wf/focus` | `#0b57d0` | focus ring, links | 6.4 · 5.5 |
| `wf/paper` · `wf/fill` · `wf/fill2` · `wf/line` | `#fff` · `#eceef0` · `#dfe2e5` · `#c7c9cc` | surfaces, grey boxes, dividers | — |

  `wf/muted` on `wf/fill2` is 4.65 — fine, but never lighter. White on `wf/ink` is 16.8.
- **Text styles** following the template's type scale (Inter, which Figma always has; load fonts before setting text): `wf/Title` 22 Bold · `wf/Heading` 17 Semibold · `wf/Body` 15 Regular, line height 22 · `wf/Label` 13 Medium · `wf/Caption` 12 Regular. No size below 12.
- **Base components** with auto layout: Button (primary, secondary), Field (default, error), List row, App bar, Tab bar or Sidebar, Image placeholder, Alert, Offline banner, Note. Tappable things are **≥ 44 pt high (iOS/web) or 48 dp (Android)** — use 48 when Android is in scope.

## Screens (one call per screen, then look)

For each screen in the inventory (§6), in core-flow order:

1. **Build** one top-level frame named with its screen ID and name, e.g. `S-03 Home`. Vertical auto layout, padding 16, gap 12, children fill width; use component instances and `wf/` styles only — no raw hex.
2. **Real content** from the HTML section and §7 microcopy — no lorem ipsum.
3. **States** sit as sibling frames to the right, inside one Section per screen: `S-03b Home — Empty`, `S-03c Home — Error`, and loading, offline, success where they apply. States that don't get a frame are listed in that screen's Note.
4. **Note** frame beside the default frame: purpose, open questions, and the accessibility notes (heading, focus order, what the screen reader says for icons and status).
5. **Screenshot-check** the frame or Section with `get_screenshot`: text clipped, overlaps, wrong order, missing states, targets under 44/48. Fix before the next screen.

Depth sets the frame count, because each Figma call is large:

| Depth | Frames |
|---|---|
| Standard | ≤ 8 frames in total (default screens plus the required empty and error states); other states as Note text |
| Deep | 12+ frames, with full state rows for the core-flow screens |

## Flows

- **Default — prototype connections:** with `use_figma`, link primary actions *On click → Navigate to* the next frame, matching the HTML links; set the first-run screen as the flow starting point.
- **Or a FigJam map:** `generate_diagram` from the §5 Mermaid flowcharts into `<Product> — Flows v<n>`. Offer it when the owner wants the map rather than a click-through.

## Finish

- `get_metadata` on each page: every screen ID from the inventory is present and named the same as the HTML.
- Write the file link into the `DESIGN_DIRECTION.md` header (`· Figma: <link>`) and §10, with the date and depth. Log any Figma-only decision in `CLARITY.md`.
- Present the link with one line on what's there (*"8 phone frames, flows as prototype links, in your drafts"*).

## If something fails

- A write is refused (seat, drafts, permissions): say so once, keep the HTML as the deliverable, and offer the manual path below.
- A `use_figma` script errors: read the error, fix that script, re-run only that screen — don't rebuild the file.
- Running low on the rate limit: stop screenshot checks, finish the frames, and tell the owner which frames weren't looked at.

## Without the connector

Say it once, then carry on with the HTML — no pressure to connect:

- *"If you want these in Figma, the html.to.design plugin can import `design/wireframes/index.html` (via its browser extension on the open page, or a URL) — you'll get editable layers to restyle."*
- Connecting the Figma connector later lets this skill build the file directly; see [CONNECTORS.md](../../../CONNECTORS.md).
