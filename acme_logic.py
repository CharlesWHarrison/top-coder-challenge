#!/usr/bin/env python3
import sys

def predict(trip_duration_days, total_receipts_amount, miles_traveled):
    # Feature transformations
    BF4  = max(0, 6   - trip_duration_days)
    BF6  = max(0, total_receipts_amount - 389.49)
    BF8  = max(0, total_receipts_amount - 1030.64)
    BF14 = max(0, trip_duration_days     - 8)
    BF66 = max(0, miles_traveled         - 70)
    
    # Regression equation
    y = (
        639.131
        - 88.7848 * BF4
        +  1.17262 * BF6
        -  1.13259 * BF8
        + 37.7531  * BF14
        +  0.445601 * BF66
    )
    return y

if __name__ == "__main__":
    # Expect exactly three args after the script name
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <trip_duration_days> <total_receipts_amount> <miles_traveled>")
        sys.exit(1)

    # Parse the inputs
    try:
        td = float(sys.argv[1])
        tr = float(sys.argv[2])
        mt = float(sys.argv[3])
    except ValueError:
        print("All three arguments must be numbers.")
        sys.exit(1)

    # Compute and print
    out = predict(td, tr, mt)
    print(out)
