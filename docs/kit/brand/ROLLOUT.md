# MakerLine brand rollout — the places only the owner can change

Everything in the repo, the docs site and the local folder is done by `build_brand.py` and the release. These are the places outside the repo that still show the old name or need a file uploaded by hand. Tick them off here.

## GitHub repository settings

- [x] **Settings → General → Repository name:** `makerline` (done 20 Oct 2026; links switched by `scripts/rename-repo-urls.sh`). Then, in the clone, run `scripts/rename-repo-urls.sh --apply` on a branch and open a pull request (switches every link and the docs site address; GitHub redirects old repo links, but not the old site address).
- [x] **About (gear icon on the repo home) → Description:** (done)
  > MakerLine — know if it's worth building, then build it right. Open-source Claude plugin: honest idea evaluation, competitors, wireframes, PRD, then build and ship with accessibility (WCAG 2.2 AA), security and tests enforced.
- [x] **About → Website:** `https://sairam5294.github.io/makerline/` (done). GitHub Pages serves the site at the repo name in lowercase; `…/MakerLine/` gives "page not found".
- [ ] **About → Topics:** set, but four are still missing: add **makerline · claude-plugin · accessibility · wcag** (they're how people searching for accessible AI tooling find it). Optional: remove `ai-agents-and-tools`.
- [ ] **Settings → General → Social preview → Upload:** `docs/kit/brand/makerline-social-preview.png` (1280 × 640).
- [x] **Settings → General → Pull Requests:** *Automatically delete head branches* (done).

## Claude plugin directory (when submitting MakerLine Idea)

- [ ] Listing reads name and description from `makerline-idea/.claude-plugin/plugin.json` and its README — already updated; nothing to type.
- [ ] If the form asks for an image: `docs/kit/brand/makerline-idea-social-preview.png`; icon `makerline-idea-mark-512.png`.

## Figma

- [ ] In Figma, rename the file **"Product Kit — Design System"** → **"MakerLine — Design System"** (click the file name at the top), then **republish** the Community listing so its title and thumbnail update. Done for you on 21 Oct 2026: the cover and Community thumbnail text inside the file, and the 6 references in the repo.
- [ ] Add the logo to the Community listing cover if you'd like: `makerline-logo@4x.png`.

## Other profiles (optional)

- [ ] GitHub profile README / pinned repos: use `makerline-logo.svg` (light) or `makerline-logo-on-dark.svg`.
- [ ] LinkedIn, portfolio: `makerline-social-preview.png` as the link image; the one-line description from `README.md` in this folder.
- [ ] Figma Community profile: same.

## Already done (for reference)

Repo and both plugins renamed · plugin IDs and commands · marketplace · READMEs with logos · docs site (favicon set, manifest, header mark in both modes, accessibility statement) · cockpit (mark, favicon, brand blue) · submission pack · brand guide and `build_brand.py` · local folder `Code_Projects/MakerLine` with `brand/`, `releases/`, archived old builds · quarterly standards scheduled task renamed.
