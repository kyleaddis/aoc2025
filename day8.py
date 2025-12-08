import sys
import math
from itertools import combinations

if len(sys.argv) != 2:
    sys.exit(1)
input = ""

with open(sys.argv[1]) as f:
    input = f.read()

input = input.split()

boxes = [eval(line) for line in input]
circuits = {frozenset([box]) for box in boxes}

box_pairs = list(combinations(boxes, 2))
box_pairs.sort(key=lambda pair: math.dist(*pair))

for i, (b1, b2) in enumerate(box_pairs):
    circuit1 = next(c for c in circuits if b1 in c)
    circuit2 = next(c for c in circuits if b2 in c)

    if circuit1 != circuit2:
        circuits.remove(circuit1)
        circuits.remove(circuit2)
        merged_circuit = circuit1 | circuit2
        circuits.add(merged_circuit)

    if i + 1 == 1000:
        sizes = sorted([len(c) for c in circuits])
        top_three = math.prod(sizes[-3:])
        print(f"Part 1: {top_three}")

    if len(circuits) == 1:
        last_pair = b1[0] * b2[0]
        print(f"Part 2: {last_pair}")
        break
