import argparse
import bz2
import sys
import math
from pathlib import Path


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def my_gen_mut_algorithm(points):
    if len(points) < 2:
        return float('inf'), None
    
    if len(points) == 2:
        return dist(points[0], points[1]), (points[0], points[1])

    def get_x(points): 
        return points[0] 
    points_sorted = sorted(points, key=get_x)

    mid = len(points_sorted) // 2
    left = points_sorted[:mid]
    right = points_sorted[mid:]

    dist_left, pair_left = my_gen_mut_algorithm(left)
    dist_right, pair_right = my_gen_mut_algorithm(right)

    if dist_left < dist_right:
        min_dist = dist_left
        closest_pair = pair_left
    else:
        min_dist = dist_right
        closest_pair = pair_right


    mid_x = points_sorted[mid][0]
    strip = [p for p in points_sorted if abs(p[0] - mid_x) < min_dist]

    def get_y(point):
        return point[1] 
    strip.sort(key=get_y)

    for i in range(len(strip)): #Mirar i entendre si es pot optimitzar o com
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            d = dist(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (strip[i], strip[j])

    return min_dist, closest_pair
    


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
