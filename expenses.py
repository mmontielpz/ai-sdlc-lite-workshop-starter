"""Expense report CLI (starter). Standard library only; Python 3.9+."""
import argparse
import csv
import sys
from decimal import Decimal, InvalidOperation


def load_expenses(path):
    """Return (rows, skipped). A row needs a category and a numeric amount; others are skipped."""
    rows, skipped = [], 0
    with open(path, newline='', encoding='utf-8') as handle:
        for record in csv.DictReader(handle):
            category = (record.get('category') or '').strip()
            try:
                amount = Decimal((record.get('amount') or '').strip())
            except InvalidOperation:
                category = ''
            if not category:
                skipped += 1
                continue
            rows.append({'date': record['date'], 'category': category, 'amount': amount})
    return rows, skipped


def total(rows):
    return sum((row['amount'] for row in rows), Decimal('0'))


def main(argv=None):
    parser = argparse.ArgumentParser(description='Summarize an expenses CSV file.')
    parser.add_argument('path', help='CSV file with date,category,amount,note columns')
    args = parser.parse_args(argv)
    rows, skipped = load_expenses(args.path)
    print(f'Total: {total(rows):.2f}')
    print(f'Rows: {len(rows)}')
    if skipped:
        print(f'Skipped rows: {skipped}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
