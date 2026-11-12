# Troubleshooting

| Symptom | Fix |
| --- | --- |
| `copilot: command not found` | Install Copilot CLI and sign in (`copilot login`); otherwise use [FALLBACK.md](FALLBACK.md). |
| `skill list` does not show `ai-sdlc-lite` | Run the `skill add --project` command from this folder (needs HTTPS access to raw.githubusercontent.com). `copilot skill remove ai-sdlc-lite` then add again. |
| Folder trust prompt | Choose "Yes" (this session only), not "remember". |
| `./check.sh: Permission denied` | `sh check.sh` or `chmod +x check.sh`. |
| `python3: command not found` | Use `python` on Windows, or install Python 3.9+. |
| `npm ci` or the build fails on an old Node | Use Node.js 20.19+ or 22.12+ (`node --version`). |
| Port already in use | Stop the other dev server, or run `npm run dev -- --host 127.0.0.1 --port 5174`. |
| Website checks fail before you changed anything | Run from `website/`; delete `website/node_modules` and rerun `npm ci`. Report it if it persists. |
| Agent edits `package.json`, the lockfile or files outside the allowed list | Decline, or `git restore website/package.json website/package-lock.json`; restate the scope. |
| Reset the website exercise | `git restore website/` and remove new files with `git status`; `.github/skills/` stays. |
| Tests fail at start | Expected: 3 of the 4 acceptance tests fail until you finish. Baseline: `python3 -B -m unittest tests.test_baseline` must pass. |
| Agent edits other files | Decline the prompt, say "only expenses.py", or `git restore <file>`. |
| Agent loops or runs long | Stop it, review `git diff`, restart with a smaller request. |
| Usage or credit limit reached | Stop; use [FALLBACK.md](FALLBACK.md). |
| Messy state | `git restore expenses.py` resets the answer. |
