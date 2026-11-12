# Acceptance criteria

Run these yourself, not only the agent:

| # | Criterion | How to check | Expected |
| --- | --- | --- | --- |
| 1 | All tests pass | `./check.sh` | `Ran 6 tests ... OK`, exit 0 |
| 2 | Feature works | `python3 expenses.py data/expenses.csv --by-category` | `rent 900.00`, `food 43.35`, `fun 42.00`, `transport 21.00`, `Total 1006.35`, `Skipped rows: 2` (one per line) |
| 3 | Default output unchanged | `python3 expenses.py data/expenses.csv` | `Total: 1006.35`, `Rows: 9`, `Skipped rows: 2` |
| 4 | Scope respected | `git status --short` | only ` M expenses.py` (no `.github/skills/`, which is git-ignored) |
| 5 | You reviewed the change | `git diff` | You can explain every line |
| 6 | One plan approval, result reported in chat | transcript | No result files required |

Completion means 1-5 observed by you. Record usage only from `/usage`; otherwise write UNKNOWN.
