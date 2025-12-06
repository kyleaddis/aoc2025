import sys

if len(sys.argv) != 2:
    sys.exit(1)
input = ""

with open(sys.argv[1]) as f:
    input = f.read()

input = input.split("\n")
matrix = [line.split() for line in input]
eles = len(matrix[0])
rows = len(matrix)
total = 0
for e in range(eles):
    exp = ""
    for r in range(rows - 2):
        exp += matrix[r][e] + matrix[-1][e]
    exp += matrix[-2][e]
    # print(sum([int(line[e]) for line in matrix if line[e].isdigit()]))
    total += eval(exp)
print(f"Part 1: {total}")
