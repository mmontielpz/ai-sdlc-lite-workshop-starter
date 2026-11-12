"""Acceptance tests for the workshop task; these FAIL until the feature is implemented."""
import pathlib
import subprocess
import sys
import unittest
from decimal import Decimal

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import expenses  # noqa: E402


class CategorySummaryTests(unittest.TestCase):
    def test_summarize_sorted_by_amount_then_name(self):
        rows = [{'date': 'd', 'category': c, 'amount': Decimal(a)}
                for c, a in [('b', '5.00'), ('a', '5.00'), ('c', '9.50'), ('b', '1.25')]]
        self.assertEqual(expenses.summarize_by_category(rows),
                         [('c', Decimal('9.50')), ('b', Decimal('6.25')), ('a', Decimal('5.00'))])

    def test_summarize_empty(self):
        self.assertEqual(expenses.summarize_by_category([]), [])

    def test_cli_by_category(self):
        done = subprocess.run([sys.executable, '-B', 'expenses.py', 'data/expenses.csv', '--by-category'],
                              cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertEqual(done.returncode, 0, done.stderr)
        lines = [line.split() for line in done.stdout.splitlines()]
        self.assertEqual(lines, [['rent', '900.00'], ['food', '43.35'], ['fun', '42.00'],
                                 ['transport', '21.00'], ['Total', '1006.35'], ['Skipped', 'rows:', '2']])

    def test_cli_default_output_unchanged(self):
        done = subprocess.run([sys.executable, '-B', 'expenses.py', 'data/expenses.csv'],
                              cwd=ROOT, capture_output=True, text=True, timeout=30)
        self.assertEqual(done.stdout.splitlines(), ['Total: 1006.35', 'Rows: 9', 'Skipped rows: 2'])


if __name__ == '__main__':
    unittest.main()
