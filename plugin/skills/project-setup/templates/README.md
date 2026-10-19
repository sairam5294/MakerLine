# {{Name}}

{{One sentence: what it is, for whom, and the one thing it does best.}}

![{{Name}} — {{main screen description}}](design/brand/screenshot.png)
<!-- Replace with a real screenshot (light mode), and write alt text that says what the screen shows. -->

## Why
{{2–3 sentences: the problem, who has it, how this is different (from EVALUATION positioning).}}

## Features
- {{Core action}} — {{one line}}
- {{Feature}} — {{one line}}
- Accessible: WCAG 2.2 AA, works with screen readers, keyboard and 200% text. [Accessibility statement]({{link}})

## Tech stack
| Layer | Technology |
|---|---|
| {{App / web}} | {{…}} |
| {{Backend / database / auth}} | {{…}} |
| {{Hosting}} | {{…}} |
Details and reasons: [`docs/product/TECH_STACK.md`](docs/product/TECH_STACK.md)

## Quick start
```bash
git clone https://github.com/{{owner}}/{{repo}}.git && cd {{repo}}
{{install command}}
cp .env.example .env.local        # then fill in the values — every line is explained in the file
{{local services command, if any}}
{{run command}}                    # opens {{http://localhost:3000}}
```
First time, on a new machine, or downloaded as ZIP? Follow [`docs/SETUP.md`](docs/SETUP.md).

## Scripts
| Command | What it does |
|---|---|
| `{{npm run dev}}` | start locally |
| `{{npm run check}}` | typecheck, lint, tests — must pass before a PR |
| `{{npm test}}` | tests only |
| `{{npm run build}}` | production build |

## Project structure
```
{{top-level tree, one line each}}
```
Where every file goes: [`docs/STRUCTURE.md`](docs/STRUCTURE.md) · All docs: [`docs/README.md`](docs/README.md)

## Contributing
Branches are named `<type>/<Mon>-<DD>-<summary>` — create one with `scripts/branch.sh fix "what changed"`. Open a pull request; checks must be green. Rules for people and AI tools: [`AGENTS.md`](AGENTS.md).

## Licence
{{MIT / proprietary}} · © {{year}} {{owner}}
