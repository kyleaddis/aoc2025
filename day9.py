import sys
import math
from itertools import combinations, pairwise

if len(sys.argv) != 2:
    sys.exit(1)
input = ""

with open(sys.argv[1]) as f:
    input = f.read()

input = input.split()

points = [(eval(line)) for line in input]
red = list(map(eval, input))


def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


pairs = list(combinations(points, 2))
pairs.sort(key=lambda pair: area(*pair), reverse=True)

print(f"Part 1: {(area(*pairs[0]))}")

path = list(pairwise(points + [points[0]]))
new_area = 0


for (prx1, pry1), (prx2, pry2) in combinations(points, 2):
    if prx1 > prx2:
        prx1, prx2 = prx2, prx1
    if pry1 > pry2:
        pry1, pry2 = pry2, pry1
    size = area((prx1, pry1), (prx2, pry2))
    if size > new_area:
        for (pgx1, pgy1), (pgx2, pgy2) in path:
            if pgx1 > pgx2:
                pgx1, pgx2 = pgx2, pgx1
            if pgy1 > pgy2:
                pgy1, pgy2 = pgy2, pgy1

            if pgx1 < prx2 and pgy1 < pry2 and pgx2 > prx1 and pgy2 > pry1:
                break
        else:
            new_area = size
print(f"Part 2: {new_area}")
