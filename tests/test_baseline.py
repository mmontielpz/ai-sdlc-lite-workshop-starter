"""Starter behavior that already works; these pass before the task begins."""
import pathlib
import sys
import unittest
from decimal import Decimal

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import expenses  # noqa: E402


class BaselineTests(unittest.TestCase):
    def test_load_skips_malformed_rows(self):
        rows, skipped = expenses.load_expenses(ROOT / 'data' / 'expenses.csv')
        self.assertEqual((len(rows), skipped), (9, 2))

    def test_total(self):
        rows, _ = expenses.load_expenses(ROOT / 'data' / 'expenses.csv')
        self.assertEqual(expenses.total(rows), Decimal('1006.35'))


if __name__ == '__main__':
    unittest.main()
