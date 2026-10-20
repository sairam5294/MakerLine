# Product Kit cockpit (kit-ui)

A small web page on your own computer that shows every Product Kit project and tells you **what to paste into Claude next**. The chat stays the engine; this is the dashboard beside it.

## Run it

```bash
python3 scripts/kit-ui.py                                # scans ~/Projects
python3 scripts/kit-ui.py --projects ~/Code --port 9000  # another folder or port
python3 scripts/kit-ui.py --no-save                      # strictly read-only (hides "save PITCH.md")
```

Open **http://127.0.0.1:8765/**. Stop it with Ctrl+C. Needs Python 3.9+ only: no installs, no internet.

## What it does

| Page | What you get |
|---|---|
| **Projects** | A card per folder with `docs/product/STATUS.md`: name, current phase, approval, next step, last updated, a *Stale* badge after 14 days |
| **Project** | Phase timeline (done, up next, waiting for you, skipped, not started, with the ★ approval gate), every `docs/**/*.md` as a readable page, and **Run next**: the folder to open and the exact prompt to paste, with a Copy button |
| **New idea** | Pitch, depth (Quick / Standard / Deep), launch markets, platforms → a ready-to-paste `/product-kit:start … — give me everything` prompt |
| **Skills** | Every skill in `plugin/skills` with the first sentence of its description |

Approval is never a prompt: when the Idea Pack is ready, Run next shows `scripts/approve.sh` to run in Terminal yourself.

## What it never does

- **Never listens beyond your computer.** It binds to `127.0.0.1` only, never `0.0.0.0`, and refuses requests that don't use that address or `localhost`.
- **Never calls an AI or any website.** No API keys, no CDN; CSS and JS are served from this folder under a strict Content-Security-Policy.
- **Never changes a project.** The one exception is opt-in: tick *Save PITCH.md into a new project folder* and it writes `<folder>/docs/product/PITCH.md` inside `--projects`, only if that file doesn't already exist. `--no-save` removes even that.
- **Never reads outside `--projects`.** Every path is resolved and checked (`../`, absolute paths and symlinks that point out are refused with 403). Only `.md` files are shown.
- **Never runs content from your files.** Markdown is rendered by a tiny built-in renderer that escapes everything; raw HTML in a document is shown as text, and only `http(s)` and in-project `.md` links become links.

## Accessibility

WCAG 2.2 AA: skip link, landmarks, one `h1` per page, visible focus, all keyboard-operable, labelled fields, errors listed in an alert and linked to the field, Copy announces "Copied", status shown with shape and words (not colour alone), ≥ 4.5:1 contrast in light and dark, 44px targets, reflows at 320px / 200% zoom, respects reduced motion.

## Files

- `scripts/kit-ui.py` — the server (reuses `scripts/portfolio.py` to find and read projects)
- `kit-ui/app.css`, `kit-ui/app.js` — styles and the Copy button
- `tests/kit-ui.test.sh` — starts it on a sample project and checks pages, traversal refusal and the 127.0.0.1 binding

## How it's tested
- `tests/kit-ui.test.sh` — 32 checks: pages load, path traversal refused, binds to 127.0.0.1 only, Host header checked. Passes on Python 3.9 (macOS default) and 3.13.
- `tests/kit-ui-a11y.mjs` (in CI) — axe-core WCAG 2.2 AA on every page in light and dark mode, skip link is the first Tab stop, no sideways scroll at 320 px. Last result: 0 violations.
- Still manual: a pass with VoiceOver on macOS (VO + arrow keys through Projects, a project page, Copy buttons and the New idea form). Note anything confusing in a GitHub issue ("Accessibility barrier" form).
