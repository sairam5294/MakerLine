#!/usr/bin/env python3
"""Build the MakerLine docs site (GitHub Pages) from the repo's own Markdown.

Why: the site must never drift from the repo. Reference pages (README, GETTING-STARTED,
the Idea Pack README, the ClubSlot example pack, CHANGELOG, LESSONS) are rendered as-is.
The only site-specific words live in docs/site/*.md (landing page, 5-minute walkthrough,
case studies, privacy) and link to the repo files they summarise, so a fact changes in one place.

    python3 scripts/build-site.py [out_dir]     default: _site/

Needs: Python 3.10+ and the `markdown` package (pip install markdown==3.10.3).
No JavaScript, no external requests, no tracking.
"""
import html
import pathlib
import re
import shutil
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/sairam5294/product-kit"
BLOB = f"{REPO}/blob/main/"
EX = "examples/idea-pack-clubslot"

SITE = "docs/site"  # hand-written site pages (Markdown; simple HTML blocks allowed via md_in_html)

# (source in repo, output page, nav label or None, page title)
PAGES = [
    (f"{SITE}/index.md", "index.html", None, "MakerLine — know if it's worth building. Then build it right."),
    (f"{SITE}/five-minutes.md", "five-minutes.html", "Start in 5 minutes", "5 minutes with MakerLine"),
    ("GETTING-STARTED.md", "getting-started.html", "Getting started", "Getting started"),
    (f"{SITE}/case-studies.md", "case-studies/index.html", "Case studies", "Case studies"),
    ("makerline-idea/README.md", "makerline-idea.html", "MakerLine Idea", "MakerLine Idea"),
    ("README.md", "overview.html", "Docs", "MakerLine — full overview"),
    ("CHANGELOG.md", "changelog.html", "Changelog", "Changelog"),
    ("LESSONS.md", "lessons.html", None, "What the kit got wrong"),
    (f"{SITE}/case-rhythmbuddy.md", "case-studies/rhythmbuddy.html", None, "Case study: RhythmBuddy"),
    (f"{SITE}/case-clubslot.md", "case-studies/clubslot.html", None, "Case study: ClubSlot"),
    (f"{SITE}/privacy.md", "privacy.html", None, "Privacy and data handling"),
    (f"{SITE}/accessibility.md", "accessibility.html", None, "Accessibility statement"),
    (f"{EX}/README.md", "example/index.html", None, "Example Idea Pack: ClubSlot"),
]
EXAMPLE_DOCS = ["ONE_PAGER", "README", "PROJECT_BRIEF", "CLARITY", "EVALUATION", "COMPETITORS",
                "DESIGN_DIRECTION", "PRD", "STATUS", "DECISIONS"]
for name in EXAMPLE_DOCS:
    src = f"{EX}/docs/product/{name}.md"
    if (ROOT / src).exists():
        label = "Index" if name == "README" else name.replace("_", " ").title()
        PAGES.append((src, f"example/{name.lower()}.html", None, f"ClubSlot — {label}"))

SRC_TO_OUT = {src: out for src, out, _, _ in PAGES}
COPY = {f"{EX}/design/wireframes/index.html": "example/wireframes/index.html"}

ASSETS = f"{SITE}/assets"  # site.css, favicon, self-hosted fonts — copied as-is to /assets

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; font-src 'self'; img-src 'self' https: data:; base-uri 'none'; form-action 'none'">
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F6F8FB" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1522" media="(prefers-color-scheme: dark)">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://sairam5294.github.io/product-kit/assets/social-preview.png">
<meta property="og:image:alt" content="MakerLine: know if it's worth building. Then build it right.">
<meta name="twitter:card" content="summary_large_image">
<title>{title}</title>
<link rel="icon" href="{root}assets/favicon.ico" sizes="48x48">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="manifest" href="{root}assets/site.webmanifest">
<link rel="preload" href="{root}assets/fonts/atkinson-hyperlegible-next-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap bar">
<a class="brand" href="{root}index.html"><picture><source srcset="{root}assets/mark-on-dark.svg" media="(prefers-color-scheme: dark)"><img src="{root}assets/favicon.svg" alt="" width="28" height="28"></picture>MakerLine</a>
<nav class="main" aria-label="Main"><ul>{nav}</ul></nav>
</div></header>
<main id="main" tabindex="-1"{main_class}>
{crumbs}{subnav}{body}
</main>
<footer class="site"><div class="wrap">
<div>
<p>Created by <a href="https://github.com/sairam5294">Sairam Mogullapalli</a>. Open source under the MIT licence.</p>
<p>Found an accessibility barrier? <a href="{repo}/issues/new?template=accessibility_barrier.yml">Tell us</a>.</p>
</div>
<nav aria-label="Footer"><ul>
<li><a href="{repo}">Source on GitHub</a></li>
<li><a href="{root}lessons.html">What the kit got wrong</a></li>
<li><a href="{root}accessibility.html">Accessibility</a></li>
<li><a href="{root}privacy.html">Privacy</a></li>
<li><a href="{repo}/issues/new/choose">Open an issue</a></li>
</ul></nav>
</div></footer>
</body>
</html>
"""


def rewrite_links(body: str, src: str, out: str) -> str:
    """Point repo-relative links at built pages, or at GitHub when the target isn't part of the site."""
    src_dir = pathlib.PurePosixPath(src).parent
    out_depth = out.count("/")

    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"[a-z][a-z0-9+.-]*:|#|//", url):
            return m.group(0)
        path, _, frag = url.partition("#")
        target = pathlib.PurePosixPath(*(src_dir / path).parts)
        norm = []
        for part in target.parts:
            if part == "..":
                if norm:
                    norm.pop()
            elif part != ".":
                norm.append(part)
        key = "/".join(norm)
        if key in SRC_TO_OUT or key in COPY:
            dest = SRC_TO_OUT.get(key) or COPY[key]
            new = "../" * out_depth + dest
        else:
            new = BLOB + key
        return f'{attr}="{html.escape(new + ("#" + frag if frag else ""), quote=True)}"'

    return re.sub(r'(href|src)="([^"]+)"', fix, body)


LIST = re.compile(r"^\s*([-*+]|\d+[.)])\s")


def gfm_lists(text: str) -> str:
    """GitHub starts a list right after a paragraph line; Python-Markdown needs a blank line first."""
    out, fence, prev = [], False, ""
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and LIST.match(line) and prev.strip() and not LIST.match(prev) \
                and not prev.startswith(("    ", "\t", "|", ">")):
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out) + "\n"


def render(src: str, out: str, title: str, nav_items, root_out: pathlib.Path) -> None:
    text = gfm_lists((ROOT / src).read_text(encoding="utf-8"))
    extensions = ["tables", "fenced_code", "toc", "sane_lists"]
    if src.startswith(SITE + "/"):
        # Site pages may group content in <div markdown="1"> blocks (cards, notes); repo docs never need it.
        extensions.append("md_in_html")
    md = markdown.Markdown(extensions=extensions,
                           extension_configs={"toc": {"permalink": False}})
    body = md.convert(text)
    # Tables scroll on their own on small screens instead of the whole page (WCAG 1.4.10 Reflow).
    body = re.sub(r"<table>", '<div class="table" role="region" tabindex="0" aria-label="Table">\n<table>', body)
    body = body.replace("</table>", "</table>\n</div>")
    # Code blocks can scroll sideways, so keyboard users must be able to focus them (WCAG 2.1.1).
    body = body.replace("<pre>", '<pre tabindex="0">')
    # A page has exactly one h1: demote extra h1s in long documents.
    first = body.find("<h1")
    if first == -1:
        body = f"<h1>{html.escape(title)}</h1>\n" + body
    else:
        # Keep the first h1 whole (open and close tag); demote only the ones after it.
        end = body.find("</h1>", first) + len("</h1>")
        head, rest = body[:end], body[end:]
        body = head + re.sub(r"<(/?)h1\b", r"<\1h2", rest)
    body = rewrite_links(body, src, out)

    depth = out.count("/")
    root = "../" * depth
    nav = []
    # Pages inside a section (case-studies/…, and the ClubSlot example documents) mark that section's nav item.
    section = "case-studies/" if out.startswith(("case-studies/", "example/")) else None
    for label, dest in nav_items:
        current = ' aria-current="page"' if dest == out or (section and dest == section + "index.html") else ""
        nav.append(f'<li><a href="{root}{dest}"{current}>{label}</a></li>')
    crumbs = subnav = ""
    if out.startswith("example/") and out != "example/index.html":
        crumbs = f'<p class="crumbs"><a href="index.html">Example: ClubSlot</a> › {html.escape(title.split("— ")[-1])}</p>\n'
    elif out == "example/index.html":
        crumbs = '<p class="crumbs"><a href="../case-studies/clubslot.html">Case study: ClubSlot</a> › The full Idea Pack</p>\n'
    elif out.startswith("case-studies/") and out != "case-studies/index.html":
        crumbs = '<p class="crumbs"><a href="index.html">Case studies</a> › ' + html.escape(title.split(": ")[-1]) + "</p>\n"
    if out.startswith("example/"):
        links = [("One-pager", "one_pager.html"), ("Evaluation", "evaluation.html"), ("Competitors", "competitors.html"),
                 ("Design direction", "design_direction.html"), ("Wireframes", "wireframes/index.html"),
                 ("PRD (draft)", "prd.html"), ("Clarity log", "clarity.html"), ("Brief", "project_brief.html")]
        here = ' aria-current="page"'
        items = [f'<li><a href="{d}"{here if "example/" + d == out else ""}>{lab}</a></li>' for lab, d in links]
        subnav = '<nav aria-label="Example documents"><ul class="subnav">' + "".join(items) + "</ul></nav>\n"
    plain = re.sub(r"<[^>]+>", "", md.convert(text.split("\n\n", 2)[1] if "\n\n" in text else text))
    desc = html.escape(" ".join(plain.split())[:155], quote=True)
    page = PAGE.format(title=html.escape(title), desc=desc, root=root, nav="".join(nav), body=body,
                       crumbs=crumbs, subnav=subnav, repo=REPO,
                       main_class=' class="home"' if out == "index.html" else (' class="wide"' if out in ("changelog.html", "lessons.html") or "example/" in out else ""))
    dest = root_out / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page, encoding="utf-8")


def main() -> None:
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "_site").resolve()
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT / ASSETS, out / "assets")
    for src, dest in COPY.items():
        if (ROOT / src).exists():
            (out / dest).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / src, out / dest)
    nav_items = [(label, dest) for _, dest, label, _ in PAGES if label]
    for src, dest, _, title in PAGES:
        render(src, dest, title, nav_items, out)
    # Old addresses from before the rename keep working: an instant redirect plus a visible link.
    for old, new in {"idea-pack.html": "makerline-idea.html"}.items():
        (out / old).write_text(
            f'<!doctype html><html lang="en"><meta charset="utf-8"><title>Moved to {new}</title>'
            f'<meta http-equiv="refresh" content="0; url={new}"><link rel="canonical" href="{new}">'
            f'<p>This page moved: <a href="{new}">MakerLine Idea</a>.</p></html>\n', encoding="utf-8")
    (out / ".nojekyll").write_text("")
    print(f"Built {len(PAGES)} pages into {out}")


if __name__ == "__main__":
    main()
