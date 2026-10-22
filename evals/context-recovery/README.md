# Context recovery eval

Does a fresh AI tool, given only a project's official context, know where the project stands? This is the direct test of MakerLine's shared-context contract (`plugin/skills/handoff/references/shared-context.md`).

## Run (about 10 minutes per tool)

1. In the project, run `python3 <kit>/scripts/context_check.py check .` and fix any FAIL.
2. Give the receiving tool **only** the official context:
   - **Folder path** (Claude Code, Cursor, Codex): open the project in a fresh session.
   - **Pack path** (ChatGPT in the browser, a phone chat): run `context_check.py pack . --task Strategy --tool ChatGPT` and attach `docs/CONTEXT_PACK.md`.
3. Paste the prompt below. Don't add anything else.
4. Save the reply as `answers-<tool>.md` (outside the repo, or in `docs/product/evals/`) and score it:
   `python3 <kit>/scripts/context_check.py score answers-<tool>.md <path-to>/context-recovery.json`
5. Count **wrong claims** by hand (anything stated as fact that the files contradict), and note tokens and time if the tool shows them. Record a row in `evals/results.md`.

## Prompt

```text
You are picking up this project with no other context. Using only the project files (or the attached
context pack), answer each question in its own section headed "## C01" … "## C10". Cite file names and
IDs (D-xx, A-xx, S-x). If something isn't in the files, say "not in the files" rather than guessing.
Read as little as you need.

C01 What is the product, and what stage is it in?
C02 What is the active task, and who owns it?
C03 What is the current strategic decision, and how confident is it?
C04 Which evidence or source IDs support that decision?
C05 Which assumptions or risks matter most, and when do they expire?
C06 Is the idea approved, and what needs the owner's approval?
C07 What was done last session, and what is half-done?
C08 What is the exact next action, and which tool does it?
C09 What was rejected or tried already, and why?
C10 Which project rules constrain the work (branches, accessibility, secrets)?
```

## Answer key format

Each project writes its own key from its files **before** running the test, and keeps it **outside the project folder** (for example `MakerLine/projects/<name>/context-recovery.json`) so the tool being tested can't read it. Keep `must_include` to the 1–3 facts that prove the tool found the right file; give alternatives in a list.

```json
{
  "project": "RhythmBuddy",
  "written": "2026-10-22",
  "cases": [
    {"id": "C01", "scenario": "New tool, first session",
     "must_include": ["RhythmBuddy", ["live", "shipped"]],
     "must_not_include": ["not approved"]}
  ]
}
```

A case passes when every `must_include` item (or one of its alternatives) appears and no `must_not_include` text does. `must_not_include` matches anywhere, including where the tool quotes a phrase to say it's absent, so use it only for phrases a correct answer would never contain. The keyword score is a floor, not the whole grade: a capable tool can hit the keywords while saying "not recorded". Always read the answers, grade each case pass / partial / fail by hand, and count wrong claims.

**Pass bar:** 9/10 cases and 0 wrong claims, on each tool and each path.
