// Accessibility check for the kit's local web UI (kit-ui).
// Why: the kit promises WCAG 2.2 AA for everything it makes, so its own UI is held to the same bar.
// Runs axe-core on every page in light and dark mode, checks the skip link is the first Tab stop,
// and checks nothing scrolls sideways at 320 px (WCAG 1.4.10 reflow).
// Usage: start `python3 scripts/kit-ui.py --projects <folder with a project> --port 8799`, then
//   node tests/kit-ui-a11y.mjs http://127.0.0.1:8799   (needs @playwright/test and @axe-core/playwright,
//   which the web starter already installs — CI runs it from starter-web/).
import { chromium } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

const base = process.argv[2] || "http://127.0.0.1:8799";
// CHROMIUM_PATH lets a machine with a pre-installed Chromium skip `npx playwright install`.
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
let problems = 0;

for (const colorScheme of ["light", "dark"]) {
  const page = await (await browser.newContext({ colorScheme })).newPage();
  await page.goto(base + "/");
  const project = await page.$eval('main a[href*="project"]', (a) => a.getAttribute("href")).catch(() => null);
  for (const path of ["/", project, "/new", "/skills"].filter(Boolean)) {
    const res = await page.goto(base + path);
    const { violations } = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"])
      .analyze();
    if (res.status() !== 200 || violations.length) {
      problems++;
      console.log(`✗ ${colorScheme} ${path}: HTTP ${res.status()} ·`, violations.map((v) => `${v.id} (${v.impact})`).join(", "));
    }
  }
  await page.keyboard.press("Tab");
  const first = await page.evaluate(() => document.activeElement?.textContent?.trim() ?? "");
  if (!/skip/i.test(first)) { problems++; console.log(`✗ ${colorScheme}: first Tab stop is "${first}", not the skip link`); }
  await page.setViewportSize({ width: 320, height: 700 });
  await page.goto(base + "/");
  const wide = await page.evaluate(() => document.documentElement.scrollWidth);
  if (wide > 320) { problems++; console.log(`✗ ${colorScheme}: page scrolls sideways at 320 px (${wide} px wide)`); }
}

await browser.close();
console.log(problems ? `kit-ui a11y: ${problems} problem(s)` : "kit-ui a11y: no WCAG 2.2 AA violations, skip link first, reflows at 320 px");
process.exit(problems ? 1 : 0);
