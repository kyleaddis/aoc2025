import sys
import operator
from functools import reduce

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
    total += eval(exp)

print(f"Part 1: {total}")

lines = input
max_len = max(len(line) for line in lines)

nums = []
cur_op = ""
total = 0

for x in range(max_len):
    cur_num = 0
    for y in range(len(lines)):
        if x < len(lines[y]) and lines[y][x].isdigit():
            cur_num = cur_num * 10 + int(lines[y][x])
        elif x < len(lines[y]) and lines[y][x] in "+*":
            cur_op = lines[y][x]

    if cur_num:
        nums.append(cur_num)
    else:
        total += sum(nums) if cur_op == "+" else eval("*".join(map(str, nums)))
        nums = []

total += sum(nums) if cur_op == "+" else eval("*".join(map(str, nums)))

print(f"Part 2: {total}")
