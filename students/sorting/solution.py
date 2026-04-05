import argparse
import bz2
import json
import sys
from pathlib import Path


def my_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = my_sort(arr[:mid])
    right = my_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=Path,
        help="Path to input .bz2 file containing JSON array of integers",
    )
    args = parser.parse_args()

    # Load instance
    try:
        with bz2.open(args.input, "rb") as f:
            data = json.load(f)
    except Exception as e:
        sys.exit(f"Error loading instance: {e}")

    if not isinstance(data, list):
        sys.exit("Invalid instance format: expected a JSON list")

    sorted_arr = my_sort(data)

    # Print result to standard output (space-separated)
    print(*(sorted_arr))


if __name__ == "__main__":
    main()
