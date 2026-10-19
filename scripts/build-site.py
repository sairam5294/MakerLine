#!/usr/bin/env python3
"""Build the Product Kit docs site (GitHub Pages) from the repo's own Markdown.

Why: the site must never drift from the repo, so it has no content of its own.
README, GETTING-STARTED, the Idea Pack README, the ClubSlot example pack,
CHANGELOG and LESSONS are rendered into one accessible static site.

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

# (source in repo, output page, nav label or None, page title)
PAGES = [
    ("README.md", "index.html", "Home", "Product Kit — the open-source designer's AI toolkit"),
    ("GETTING-STARTED.md", "getting-started.html", "Getting started", "Getting started"),
    ("idea-pack/README.md", "idea-pack.html", "Idea Pack", "Idea Pack"),
    (f"{EX}/README.md", "example/index.html", "Example", "Example Idea Pack: ClubSlot"),
    ("CHANGELOG.md", "changelog.html", "Changelog", "Changelog"),
    ("LESSONS.md", "lessons.html", "Lessons", "What the kit got wrong"),
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

CSS = """
:root{--bg:#FFFFFF;--surface:#F7F7F8;--text:#16161A;--muted:#5C5C66;--border:#C4C4CC;--link:#174CAB;--focus:#1F5FD1;--code:#EDEDEF}
@media (prefers-color-scheme:dark){:root{--bg:#16161A;--surface:#2A2A31;--text:#F7F7F8;--muted:#C4C4CC;--border:#5C5C66;--link:#A6C4FF;--focus:#7AA7FF;--code:#2A2A31}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:1.0625rem/1.6 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans",sans-serif}
a{color:var(--link);text-underline-offset:.15em}
a:focus-visible,summary:focus-visible,[tabindex]:focus-visible{outline:3px solid var(--focus);outline-offset:2px;border-radius:2px}
.skip{position:absolute;left:-999px;top:0;background:var(--bg);padding:.75rem 1rem;z-index:10}
.skip:focus{left:1rem;top:1rem}
header{border-bottom:1px solid var(--border);background:var(--surface)}
.wrap{max-width:70rem;margin:0 auto;padding:0 1rem}
.bar{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1.5rem;min-height:3.5rem}
.brand{font-weight:700;color:var(--text);text-decoration:none;padding:.5rem 0}
nav ul{display:flex;flex-wrap:wrap;gap:.25rem 1rem;list-style:none;margin:0;padding:0}
nav a{display:inline-block;padding:.6rem .25rem;min-height:44px}
nav a[aria-current="page"]{font-weight:700;color:var(--text);text-decoration-thickness:3px}
main{max-width:46rem;margin:0 auto;padding:2rem 1rem 4rem}
main.wide{max-width:70rem}
h1{font-size:2rem;line-height:1.2;margin-top:0}
h2{margin-top:2.5rem;font-size:1.5rem;line-height:1.25}
h3{margin-top:2rem;font-size:1.2rem}
code{background:var(--code);padding:.1em .3em;border-radius:4px;font-size:.92em}
pre{background:var(--code);padding:1rem;border-radius:8px;overflow:auto}
pre code{background:none;padding:0}
.table{overflow-x:auto;margin:1rem 0}
table{border-collapse:collapse;width:100%;font-size:.95rem}
th,td{border:1px solid var(--border);padding:.5rem .6rem;text-align:left;vertical-align:top}
th{background:var(--surface)}
blockquote{margin:1rem 0;padding:.5rem 1rem;border-left:4px solid var(--border);color:var(--muted)}
.crumbs{font-size:.95rem;color:var(--muted)}
.subnav{display:flex;flex-wrap:wrap;gap:.25rem 1rem;padding:0;list-style:none;margin:1rem 0 2rem;font-size:.95rem}
.subnav a{display:inline-block;min-height:44px;padding:.6rem 0}
footer{border-top:1px solid var(--border);color:var(--muted);font-size:.9rem}
footer .wrap{padding:1.5rem 1rem}
img{max-width:100%;height:auto}
main p,main li,main td,main th,main h1,main h2,main h3,main a{overflow-wrap:anywhere}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self' https: data:; base-uri 'none'; form-action 'none'">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" href="data:,">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header><div class="wrap bar">
<a class="brand" href="{root}index.html">Product Kit</a>
<nav aria-label="Main"><ul>{nav}</ul></nav>
</div></header>
<main id="main" tabindex="-1"{main_class}>
{crumbs}{subnav}{body}
</main>
<footer><div class="wrap">
Created by <a href="https://github.com/sairam5294">Sairam Mogullapalli</a> · Open source under the MIT licence · <a href="{repo}">Source on GitHub</a> · Built from the repository's own files; edit them there.
Found an accessibility barrier? <a href="{repo}/issues/new?title=Accessibility%20barrier">Tell us</a>.
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
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"],
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
        head, rest = body[:first + 3], body[first + 3:]
        body = head + re.sub(r"<(/?)h1\b", r"<\1h2", rest)
    body = rewrite_links(body, src, out)

    depth = out.count("/")
    root = "../" * depth
    nav = []
    for label, dest in nav_items:
        current = ' aria-current="page"' if dest == out or (dest == "example/index.html" and out.startswith("example/")) else ""
        nav.append(f'<li><a href="{root}{dest}"{current}>{label}</a></li>')
    crumbs = subnav = ""
    if out.startswith("example/") and out != "example/index.html":
        crumbs = f'<p class="crumbs"><a href="index.html">Example: ClubSlot</a> › {html.escape(title.split("— ")[-1])}</p>\n'
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
                       main_class=' class="wide"' if out in ("changelog.html", "lessons.html") or "example/" in out else "")
    dest = root_out / out
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page, encoding="utf-8")


def main() -> None:
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "_site").resolve()
    if out.exists():
        shutil.rmtree(out)
    (out / "assets").mkdir(parents=True)
    (out / "assets" / "site.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    for src, dest in COPY.items():
        if (ROOT / src).exists():
            (out / dest).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / src, out / dest)
    nav_items = [(label, dest) for _, dest, label, _ in PAGES if label]
    for src, dest, _, title in PAGES:
        render(src, dest, title, nav_items, out)
    (out / ".nojekyll").write_text("")
    print(f"Built {len(PAGES)} pages into {out}")


if __name__ == "__main__":
    main()
