import sys
import re

if len(sys.argv) != 2:
    sys.exit(1)
codes = ""

with open(sys.argv[1]) as f:
    codes = f.read()

ranges = [[int(r.split("-")[0]), int(r.split("-")[1])] for r in codes.split(",")]

invalid = []
invalid_part2 = []

for r in ranges:
    start = r[0]
    end = r[1]
    length = len(str(start))
    for n in range(start, end + 1):
        if re.match(r"\b(\d+)\1\b", str(n)):
            invalid.append(n)
        if re.match(r"\b(\d+)\1+\b", str(n)):
            invalid_part2.append(n)
print(f"Part 1: {sum(invalid)}")
print(f"Part 2: {sum(invalid_part2)}")
