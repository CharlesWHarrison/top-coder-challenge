#!/usr/bin/env bash
# run.sh — wrapper around acme_logic.py using positional params directly

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <trip_duration_days> <total_receipts_amount> <miles_traveled>" >&2
  exit 1
fi

python3 "$(dirname "$0")/acme_logic.py" "$1" "$2" "$3"
