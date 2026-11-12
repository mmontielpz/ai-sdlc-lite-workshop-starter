# Engineering challenge: category summary

`expenses.py` prints a total. Add a `--by-category` option and the function behind it.

**Request to give Copilot** (it invokes the Skill, which makes the agent inspect, plan, and stop for approval):

> Use the /ai-sdlc-lite skill. In `expenses.py`, add `summarize_by_category(rows)` and a `--by-category` flag, as described in TASK.md and ACCEPTANCE.md. You may change only `expenses.py`. Inspect first and propose a plan with the exact check `./check.sh`. Stop for plan approval. After approval implement, run the check, report the result in chat, and stop.

**Behavior**
- `summarize_by_category(rows)` returns `[(category, Decimal_total), ...]` sorted by total descending, then by category name.
- `python3 expenses.py data/expenses.csv --by-category` prints one line per category (`name` then amount with two decimals), then a `Total` line, then `Skipped rows: N` when N > 0.
- Without the flag, output is unchanged.

**Constraints**: change only `expenses.py`; do not edit tests or data; no new dependencies.
