import sys

if len(sys.argv) != 2:
    sys.exit(1)
input = ""

with open(sys.argv[1]) as f:
    input = f.read()

input = input.split()

fresh = []
foods = []

for i, line in enumerate(input):
    if "-" in line:
        fresh.append([int(line.split("-")[0]), int(line.split("-")[1])])
    else:
        foods = list(map(int, input[i::]))
        break

is_fresh = []
for food in foods:
    for f in fresh:
        if food >= f[0] and food <= f[1]:
            is_fresh.append(1)
            break

ranges = []
for start, stop in fresh:
    merged_ranges = []
    for current_start, current_stop in ranges:
        if start <= current_stop and stop >= current_start:
            start = min(start, current_start)
            stop = max(stop, current_stop)
        else:
            merged_ranges.append([current_start, current_stop])
    merged_ranges.append([start, stop])
    ranges = merged_ranges

total_range = sum([r[1] - r[0] + 1 for r in ranges])


print(f"Part 1: {sum(is_fresh)}")
print(f"Part 2: {total_range}")
