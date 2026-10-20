# Screen reader test script (VoiceOver first)

Automated checks (axe) catch about a third to half of accessibility problems. This script covers the rest on the docs site and the cockpit. It takes about 30 minutes. Do it before each release that changes the site, and record the result in the table at the end.

## Set up

| Device | Turn on | Basic keys |
|---|---|---|
| Mac (Safari) | Cmd + F5, or System Settings → Accessibility → VoiceOver | VO = Control + Option. VO + Right arrow: next item. VO + U: rotor (headings, links, landmarks). VO + Space: activate |
| iPhone (Safari) | Settings → Accessibility → VoiceOver, or triple-click the side button if set up | Swipe right: next item. Double-tap: activate. Two-finger rotate: rotor |
| Windows (NVDA, free) | Ctrl + Alt + N after installing from nvaccess.org | H: next heading. D: next landmark. Tab: next link or button |
| Android (TalkBack) | Settings → Accessibility → TalkBack | Swipe right: next. Double-tap: activate |

Test the live site: https://sairam5294.github.io/makerline/. Use a real phone for the iPhone and TalkBack passes; simulators miss gestures.

## Checks

**1. Arriving on the home page**
- The page title is announced: "MakerLine — know if it's worth building…".
- The first Tab press lands on "Skip to content". Activating it moves to the main content, and VoiceOver reads the headline.

**2. Landmarks and headings (rotor)**
- Landmarks: banner (header), navigation "Main", main, the "Language" navigation, content info (footer) and the three footer navigations "Learn", "Trust", "Project".
- Headings: one level-1 heading per page, then level 2 for each section. No skipped levels that change the meaning.

**3. Header controls**
- The theme button says "Switch to dark theme". After you activate it, it says "Switch to light theme", and the page colours change.
- On a phone-width window, "Menu" is announced as a button, collapsed. Activating it says "expanded" and the links follow. Escape closes it and returns focus to the button.
- The GitHub icon link says "MakerLine on GitHub".

**4. The verdict card and demo**
- The hero card reads in order: file path, "Pivot", "Medium-low confidence", then each label and value.
- The demo reads as: "You", the command, a list of 5 steps, then the result and the "Open the full one-pager" link. Nothing is announced twice.
- "Replay" is a button and doesn't move focus.

**5. Diagrams and chart**
- The six-stop line reads as an ordered list of 6 items, with the approval step as item 4.
- The flow diagram reads as three groups with headings ("What goes in", the core, "What comes out"). The connecting lines are silent.
- The token chart is announced as an image with a title and a description that includes all three numbers and the target. On a phone-width window, it reads as a list instead.

**6. Tables**
- In "MakerLine or MakerLine Idea?" and "Why not just ask Claude?", VO + Control + Option + arrow keys move by cell, and the column headers are announced.
- Wide tables on the changelog scroll inside their own region, which is announced as "Table".

**7. Long pages**
- On the overview page, the "On this page" control is announced as collapsed or expanded. Its links jump to the right heading, and VoiceOver reads the heading after the jump.
- Code blocks: "Copy code" is a button. Activating it announces "Code copied to clipboard".

**8. Languages**
- On the Hindi page, VoiceOver switches to a Hindi voice for the content (the page says `lang="hi"`). The language links are read in their own language.
- On the Spanish page, the same with a Spanish voice.

**9. Zoom and text size**
- Zoom to 200% (Cmd + plus) and 400% on a 1280 px window. Nothing overlaps or is cut off, and there's no sideways scrolling except inside tables and code.
- On the iPhone, set the largest text size: the site still reads in order.

**10. Reduced motion**
- With "Reduce motion" on (System Settings → Accessibility → Display), nothing animates and everything shows complete.

## Record

| Date | Tester | Device + screen reader | Pages | Problems found | Issue links |
|---|---|---|---|---|---|
| | | | | | |

Report every problem as an accessibility barrier issue, and quote what the screen reader said, word for word.
