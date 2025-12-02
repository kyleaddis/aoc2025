import sys

if len(sys.argv) != 2:
    sys.exit(1)
codes = ""

with open(sys.argv[1]) as f:
    codes = f.read()

current = 50
crosses = 0
zeros = 0
for c in codes.split():
    d = c[0]
    v = int(c[1::])

    if d == "R":
        for n in range(0, v):
            current -= 1
            if current < 0:
                current = 99
            elif current == 0:
                crosses += 1
    else:
        for n in range(0, v):
            current += 1
            if current > 99:
                current = 0
                crosses += 1
    if current == 0:
        zeros += 1

print(f"Part 1: {zeros}")
print(f"Part 2: {crosses}")
