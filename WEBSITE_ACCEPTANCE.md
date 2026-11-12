# Website acceptance criteria

Check these yourself, not only the agent. Run from the repository root.

| # | Criterion | How to check | Expected |
| --- | --- | --- | --- |
| 1 | Starter was healthy | before changes: `(cd website && npm run lint && npm run build)` | both exit 0 |
| 2 | Still healthy | after changes: same command | both exit 0 |
| 3 | Page runs | `cd website && npm run dev -- --host 127.0.0.1`, open the printed `http://127.0.0.1:...` URL | page loads; stop with Ctrl+C |
| 4 | Your content and theme | look at the page | event name, colors and text are yours (fictional data) |
| 5 | Responsive | browser dev tools at about 375 px and at desktop width | no horizontal scrolling at 375 px; text readable; layout adapts |
| 6 | Assets resolve | browser console / page | no broken images (starter placeholders only) |
| 7 | No new dependencies | `git diff --stat -- website/package.json website/package-lock.json` | empty output |
| 8 | Scope respected | `git status --short` | only files under `website/src/`, `website/index.html`, `website/tailwind.config.js` (`.github/skills/` and `node_modules/` are git-ignored) |
| 9 | You reviewed the change | `git diff` | you can explain it |
| 10 | One plan approval, result in chat | transcript | no result files required |

Completion means 1-9 observed by you. Responsive appearance is checked by eye in the browser; lint and build do not prove it. Record usage only from `/usage`; otherwise write UNKNOWN.
