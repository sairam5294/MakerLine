# Publishing the kit's Figma library to Community

**Published 2026-10-14:** https://www.figma.com/community/file/1692097443572763844/makerline-design-system

The file **"Product Kit — Design System"** (Primitives, Semantic Light/Dark, Dimensions, type styles; Button, TextField, ScreenState bound to variables) is published on Figma Community so anyone using the kit can duplicate it. Publisher profile: https://www.figma.com/@sairammogullapa

## Listing copy (paste into the publish dialog)

**Name:** Product Kit — Design System

**Description:**
A small, accessible design system that matches the MakerLine starters (Expo + Supabase, Next.js). Variables in three collections — Primitives, Semantic (Light and Dark modes) and Dimensions — generated from one `design/tokens.json` in W3C Design Tokens format, so Figma and code never drift. Five type styles. Button, TextField and ScreenState component sets bound to variables, with every colour pair contrast-checked for WCAG 2.2 AA in both modes.

Duplicate it, rename it for your product, then sync `tokens.json` from your copy (the kit's `design-system` skill explains both directions). Part of the open-source MakerLine: https://github.com/sairam5294/product-kit

**Tags:** design system, design tokens, accessibility, wcag, dark mode, variables, expo, react native, nextjs, starter

**Category:** UI kits / Design systems

## Steps (owner only, about 5 minutes)
1. Open the file in Figma → **Share** → **Publish to Community** (first time: Figma asks you to set up a Community profile; it is already at the URL above).
2. Paste the name, description and tags. Thumbnail: right-click the 1920×1080 frame **Community thumbnail** on the Cover page → Set as thumbnail, then choose "Use file thumbnail" (Figma requires 1920×1080; the old 1028×290 Cover frame crops badly). Author: your individual profile, not a team. Support contact: the GitHub issues page.
3. Category: Libraries → UI kits. (Figma applies its standard Community licence; there is no licence picker in the dialog.)
4. Publish. Copy the Community link (`https://www.figma.com/community/file/…`).
5. Replace the two links in the kit with it — `README.md` ("What's inside" table) and `plugin/skills/design-system/references/tokens-figma-sync.md` — then `./scripts/release-kit.sh 0.6.1 "Figma library published to Community"`.

## Keeping it current
When `design/tokens.json` changes, update the Figma file (Option A or B in `tokens-figma-sync.md`) and click **Publish update** in Figma; Community users see the new version.
