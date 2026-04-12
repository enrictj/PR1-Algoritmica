import argparse
import bz2
import sys
import math
from pathlib import Path


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def my_gen_mut_algorithm(points):
    def get_x(points):
        return points[0]

    def get_y(points):
        return points[1]

    points_sorted = sorted(points, key=get_x)

    def _rec(points_sorted):
        n = len(points_sorted)
        if n <= 3:
            min_dist = float('inf')
            closest_pair = (None, None)
            for i in range(n):
                for j in range(i + 1, n):
                    d = dist(points_sorted[i], points_sorted[j])
                    if d < min_dist:
                        min_dist = d
                        closest_pair = (points_sorted[i], points_sorted[j])
            return min_dist, closest_pair

        mid = n // 2
        mid_x = points_sorted[mid][0]

        dist_left, pair_left   = _rec(points_sorted[:mid])
        dist_right, pair_right = _rec(points_sorted[mid:])

        if dist_left < dist_right:
            min_dist, closest_pair = dist_left, pair_left
        else:
            min_dist, closest_pair = dist_right, pair_right

        strip = []
        for point in points_sorted:
            if abs(point[0] - mid_x) < min_dist:
                strip.append(point)
        strip.sort(key=get_y)

        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] >= min_dist:
                    break
                d = dist(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    closest_pair = (strip[i], strip[j])

        return min_dist, closest_pair

    return _rec(points_sorted)
    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="Input .bz2 file")
    args = parser.parse_args()

    try:
        with bz2.open(args.input, "rb") as f:
            content = f.read().decode("utf-8")
    except Exception as e:
        sys.exit(f"Error loading instance: {e}")

    points = []
    for line in content.splitlines():
        if line.strip():
            points.append(list(map(float, line.split())))

    if len(points) < 2:
        print(0.0)
    else:
        d, pair = my_gen_mut_algorithm(points)
        print(d)
        print(f"{pair[0][0]} {pair[0][1]}")
        print(f"{pair[1][0]} {pair[1][1]}")


if __name__ == "__main__":
    main()
