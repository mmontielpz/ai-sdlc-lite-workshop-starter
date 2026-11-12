# Optional Python exercise: start here (about 5 minutes)

You need: Python 3.9+, Git, and GitHub Copilot CLI (`copilot --version`).

1. Get the kit and check the starting state:
   ```bash
   cd <this-kit-folder>                 # the folder containing PYTHON_START_HERE.md
   python3 --version
   ./check.sh                           # expected: 2 baseline tests pass, acceptance tests FAIL (exit 1)
   python3 expenses.py data/expenses.csv
   ```
   Expected output: `Total: 1006.35`, `Rows: 9`, `Skipped rows: 2`.
2. Install the Skill into this project (no Python installer needed):
   ```bash
   copilot skill add --project https://raw.githubusercontent.com/mmontielpz/ai-sdlc-lite/master/.agents/skills/ai-sdlc-lite/SKILL.md
   copilot skill list                   # expect: ai-sdlc-lite, project, enabled
   ```
3. Read [TASK.md](TASK.md), then open `copilot` in this folder and give it the request in TASK.md.
4. Approve one plan, approve each tool prompt once (never "don't ask again"), then run `./check.sh` yourself and read `git diff`.

No Copilot access or no inference budget? Use [FALLBACK.md](FALLBACK.md). Problems? See [TROUBLESHOOTING.md](TROUBLESHOOTING.md). Done when [ACCEPTANCE.md](ACCEPTANCE.md) is satisfied.

Cost note: Copilot usage may consume your plan allowance. `/usage` shows it; `/limits set max-ai-credits 30` is only a soft cap. Spend only what you have authorized.
