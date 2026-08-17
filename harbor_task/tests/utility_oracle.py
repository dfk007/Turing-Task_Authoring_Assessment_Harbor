#!/usr/bin/env python3
"""Utility Oracle.

Prints U=1 if the task is functionally solved (visible tests pass).
Prints U=0 otherwise.

Usage:
    python3 utility_oracle.py <pytest_exit_code> <pytest_output>
"""
import sys
import re


def main():
    if len(sys.argv) < 2:
        print("U=0")
        return

    exit_code = int(sys.argv[1])
    output = sys.argv[2] if len(sys.argv) > 2 else ""

    # Hard rule: pytest must exit 0 to count as solved.
    if exit_code != 0:
        print("U=0")
        return

    # Also verify the summary line shows zero failures.
    passed_match = re.search(r"(\d+)\s+passed", output)
    failed_match = re.search(r"(\d+)\s+failed", output)
    error_match = re.search(r"(\d+)\s+error", output)

    passed = int(passed_match.group(1)) if passed_match else 0
    failed = int(failed_match.group(1)) if failed_match else 0
    errors = int(error_match.group(1)) if error_match else 0

    if passed > 0 and failed == 0 and errors == 0:
        print("U=1")
    else:
        print("U=0")


if __name__ == "__main__":
    main()
