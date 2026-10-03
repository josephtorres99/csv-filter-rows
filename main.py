"""CSV Filter Rows — Filter CSV rows by a column equals or contains a value."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='csv_filter_rows',
        description='Filter CSV rows by a column equals or contains a value.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('CSV Filter Rows')
    print('A where-clause for a CSV.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
