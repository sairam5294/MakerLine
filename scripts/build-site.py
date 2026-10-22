#!/usr/bin/env python3
"""Build the MakerLine docs site (GitHub Pages) from the repo's own Markdown.

Why: the site must never drift from the repo. Reference pages (README, GETTING-STARTED,
the Idea Pack README, the ClubSlot example pack, CHANGELOG, LESSONS) are rendered as-is.
The only site-specific words live in docs/site/*.md (landing page, 5-minute walkthrough,
case studies, privacy) and link to the repo files they summarise, so a fact changes in one place.

    python3 scripts/build-site.py [out_dir]     default: _site/

Needs: Python 3.10+ and the `markdown` package (pip install markdown==3.10.3).
No external requests and no tracking. Two small scripts are progressive enhancements only (theme switch,
mobile menu, copy buttons, contents panel); every page reads and works fully without them.
"""
import html
import pathlib
import re
import shutil
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/sairam5294/makerline"
BLOB = f"{REPO}/blob/main/"
EX = "examples/idea-pack-clubslot"

SITE = "docs/site"  # hand-written site pages (Markdown; simple HTML blocks allowed via md_in_html)

# (source in repo, output page, nav label or None, page title)
PAGES = [
    (f"{SITE}/index.md", "index.html", None, "MakerLine — know if it's worth building. Then build it right."),
    (f"{SITE}/five-minutes.md", "five-minutes.html", "Start in 5 minutes", "5 minutes with MakerLine"),
    (f"{SITE}/hi/index.md", "hi/index.html", None, "MakerLine — पहले जानिए कि यह बनाने लायक़ है या नहीं। फिर सही तरीक़े से बनाइए।"),
    (f"{SITE}/es/index.md", "es/index.html", None, "MakerLine — Descubre si vale la pena construirlo. Luego constrúyelo bien."),
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

ASSETS = f"{SITE}/assets"  # site.css, theme.js, site.js, favicon, self-hosted fonts — copied as-is to /assets
BRAND = "docs/kit/brand"   # logo SVGs, copied to /assets/brand so README logos render on the site
RAW_BRAND = "https://raw.githubusercontent.com/sairam5294/makerline/main/docs/kit/brand/"
PORTFOLIO = "https://www.sairammogullapalli.com/"

# A small label above each page title, so people always know what kind of page they're on.
# The home page is also written in Hindi and Spanish (AI-translated, open to native-speaker fixes).
LANGS = {"index.html": "en", "hi/index.html": "hi", "es/index.html": "es"}
HOMES = ("index.html", "hi/index.html", "es/index.html")

EYEBROWS = {"five-minutes.html": "Guide", "getting-started.html": "Guide", "overview.html": "Reference",
            "makerline-idea.html": "Plugin", "changelog.html": "Release notes", "lessons.html": "Honesty log",
            "privacy.html": "Trust", "accessibility.html": "Trust", "case-studies/index.html": "Proof", "404.html": "Error 404"}

PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' https: data:; base-uri 'none'; form-action 'none'">
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F6F8FB" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0D1522" media="(prefers-color-scheme: dark)">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://sairam5294.github.io/makerline/assets/social-preview.png">
<meta property="og:image:alt" content="MakerLine: know if it's worth building. Then build it right.">
<meta name="twitter:card" content="summary_large_image">
<meta name="author" content="Sairam Mogullapalli">{alternates}
<title>{title}</title>
<link rel="icon" href="{root}assets/favicon.ico" sizes="48x48">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="manifest" href="{root}assets/site.webmanifest">
<link rel="preload" href="{root}assets/fonts/atkinson-hyperlegible-next-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/site.css">
<script src="{root}assets/theme.js"></script>
<script src="{root}assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap bar">
<a class="brand" href="{root}index.html"><img class="on-light" src="{root}assets/favicon.svg" alt="" width="28" height="28"><img class="on-dark" src="{root}assets/mark-on-dark.svg" alt="" width="28" height="28">MakerLine</a>
<nav class="main" aria-label="Main"><ul id="site-nav">{nav}</ul></nav>
<div class="tools"><a class="icon-btn" href="{repo}" aria-label="MakerLine on GitHub"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.87-1.37-3.87-1.37-.53-1.33-1.28-1.69-1.28-1.69-1.05-.71.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.19-3.1-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.84 1.19 3.1 0 4.42-2.7 5.39-5.26 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5Z"/></svg></a></div>
</div></header>
<main id="main" tabindex="-1"{main_class}>
{content}
</main>
<footer class="site"><div class="wrap">
<div class="foot-brand">
<p class="foot-name"><img class="on-light" src="{root}assets/favicon.svg" alt="" width="24" height="24"><img class="on-dark" src="{root}assets/mark-on-dark.svg" alt="" width="24" height="24">MakerLine</p>
<p>Know if it's worth building. Then build it right.</p>
<p>Created by <a href="{portfolio}">Sairam Mogullapalli</a>, Head of Product Design. Open source under the MIT licence.</p>
<p>Home page in <a href="{root}index.html" lang="en" hreflang="en">English</a> · <a href="{root}hi/index.html" lang="hi" hreflang="hi">हिन्दी</a> · <a href="{root}es/index.html" lang="es" hreflang="es">Español</a></p>
</div>
<nav aria-labelledby="f-learn"><h2 id="f-learn">Learn</h2><ul>
<li><a href="{root}five-minutes.html">Start in 5 minutes</a></li>
<li><a href="{root}getting-started.html">Getting started</a></li>
<li><a href="{root}overview.html">Full docs</a></li>
<li><a href="{root}changelog.html">Changelog</a></li>
</ul></nav>
<nav aria-labelledby="f-trust"><h2 id="f-trust">Trust</h2><ul>
<li><a href="{root}lessons.html">What the kit got wrong</a></li>
<li><a href="{root}accessibility.html">Accessibility</a></li>
<li><a href="{root}privacy.html">Privacy</a></li>
<li><a href="{repo}/issues/new?template=accessibility_barrier.yml">Report a barrier</a></li>
</ul></nav>
<nav aria-labelledby="f-proj"><h2 id="f-proj">Project</h2><ul>
<li><a href="{repo}">Source on GitHub</a></li>
<li><a href="{repo}/issues/new/choose">Open an issue</a></li>
<li><a href="{portfolio}">About the maker</a></li>
<li><a href="#main">Back to top</a></li>
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
        if attr == "src" and url.startswith(RAW_BRAND):
            return f'src="{"../" * out_depth}assets/brand/{url[len(RAW_BRAND):]}"'
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
        if attr == "src" and key.startswith(BRAND + "/"):
            return f'src="{"../" * out_depth}assets/brand/{key[len(BRAND) + 1:]}"'
        if key in SRC_TO_OUT or key in COPY:
            dest = SRC_TO_OUT.get(key) or COPY[key]
            new = "../" * out_depth + dest
        else:
            new = BLOB + key
        return f'{attr}="{html.escape(new + ("#" + frag if frag else ""), quote=True)}"'

    body = re.sub(r'(href|src)="([^"]+)"', fix, body)
    # Logos drawn for light backgrounds get a dark-theme twin; CSS shows the one that matches the theme.
    return re.sub(r'<img src="([^"]*assets/brand/[a-z-]+-logo)\.svg"([^>]*)>',
                  r'<img class="on-light" src="\1.svg"\2><img class="on-dark" src="\1-on-dark.svg"\2>', body)


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
    # The README demo GIF isn't needed on the site: the home page has the same demo, shorter and replayable.
    body = re.sub(r'<p><img[^>]*makerline-demo\.gif[^>]*></p>\n?', "", body)

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

    if out in HOMES:
        content, main_class = body, ' class="home"'
    else:
        # Page head: a small label and reading time above the title, so long documents feel navigable.
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        label = EYEBROWS.get(out) or ("Case study" if out.startswith("case-studies/") else
                                      "Example Idea Pack" if out.startswith("example/") else "")
        minutes = f"{max(1, round(words / 220))} min read" if words >= 300 else ""
        meta = " · ".join(x for x in (label, minutes) if x)
        eyebrow = f'<p class="eyebrow">{html.escape(meta)}</p>\n'
        h1_end = body.find("</h1>") + len("</h1>")
        head, rest = body[:h1_end], body[h1_end:]
        if len(re.sub(r"<[^>]+>", "", head[:head.find("<h1")])) > 200:  # title isn't near the top: keep the flow
            head, rest = "", body
        # Contents panel for long pages: their second-level headings, as a list of jump links.
        heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', rest)
        toc = ""
        if len(heads) >= 4:
            items = "".join(f'<li><a href="#{i}">{re.sub(r"<[^>]+>", "", h)}</a></li>' for i, h in heads)
            toc = (f'<aside class="toc" aria-label="On this page"><details><summary>On this page '
                   f'<span class="count">{len(heads)} sections</span></summary><ol>{items}</ol></details></aside>\n')
        content = (f'<div class="page-head">{crumbs}{eyebrow}{head}</div>\n{toc}'
                   f'<div class="doc">{subnav}{rest}</div>')
        wide = out in ("changelog.html", "lessons.html") or "example/" in out
        classes = [c for c, on in (("wide", wide), ("has-toc", bool(toc))) if on]
        main_class = f' class="{" ".join(classes)}"' if classes else ""
    alternates = ""
    if out in HOMES:  # tell search engines and browsers the three home pages are translations of each other
        site = "https://sairam5294.github.io/makerline/"
        alternates = "".join(f'\n<link rel="alternate" hreflang="{LANGS[h]}" href="{site}{h.replace("index.html", "")}">'
                             for h in HOMES) + f'\n<link rel="alternate" hreflang="x-default" href="{site}">'
    page = PAGE.format(title=html.escape(title), desc=desc, root=root, nav="".join(nav), content=content,
                       repo=REPO, portfolio=PORTFOLIO, main_class=main_class, lang=LANGS.get(out, "en"),
                       alternates=alternates)
    dest = root_out / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page, encoding="utf-8")


def main() -> None:
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "_site").resolve()
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT / ASSETS, out / "assets")
    (out / "assets/brand").mkdir()
    for f in [*(ROOT / BRAND).glob("*.svg"), *(ROOT / BRAND).glob("*.gif")]:
        shutil.copy2(f, out / "assets/brand" / f.name)
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
    # Page not found: GitHub Pages serves 404.html at any missing address, so its links are absolute.
    render(f"{SITE}/404.md", "404.html", "Page not found", nav_items, out)
    nf = (out / "404.html").read_text(encoding="utf-8")
    nf = re.sub(r'(href|src|srcset)="(?![a-z]+:|#|/)', r'\1="/makerline/', nf)
    (out / "404.html").write_text(nf, encoding="utf-8")
    (out / ".nojekyll").write_text("")
    print(f"Built {len(PAGES)} pages into {out}")


if __name__ == "__main__":
    main()
