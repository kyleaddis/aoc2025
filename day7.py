import sys

if len(sys.argv) != 2:
    sys.exit(1)
input = ""

with open(sys.argv[1]) as f:
    input = f.read()

input = input.split()

splits = 0
start = input[0].index("S")
beams = [0] * len(input[0])
beams[start] = 1
for row in range(len(input)):
    for col in range(len(input[0])):
        if input[row][col] == "^" and beams[col]:
            beams[col - 1] += beams[col]
            beams[col + 1] += beams[col]
            beams[col] = 0
            splits += 1

print(f"Part 1: {splits}")
print(f"Part 2: {sum(beams)}")
