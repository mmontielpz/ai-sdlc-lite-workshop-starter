#!/bin/sh
# Runs every deterministic test. Exit 0 only when all pass.
cd "$(dirname "$0")" || exit 2
python3 -B -m unittest discover -s tests
