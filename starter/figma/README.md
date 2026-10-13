# Code Connect (Figma ↔ code components)

Links the components in the **Product Kit — Design System** Figma file to the real components in `src/components/`.
In Figma Dev Mode, selecting a Button then shows `<Button label=… />` from this codebase instead of generic CSS.

Figma file: https://www.figma.com/design/Vjdm4Jlw4SnV5Prtaz1IFP

**Needs a Figma Organization or Enterprise plan** (Full or Dev seat). On Pro/Starter these files do nothing;
design-qa and handoff still work through the Figma connector.

Publish (once you're on a supported plan):
```bash
export FIGMA_ACCESS_TOKEN=…   # personal access token: Code Connect = Write, File content = Read
npx @figma/code-connect@latest connect publish
```
If you duplicate the Figma file for a new product, update the `// url=` line at the top of each file.
