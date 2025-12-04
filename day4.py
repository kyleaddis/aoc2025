from copy import deepcopy
import sys

if len(sys.argv) != 2:
    sys.exit(1)
grid = ""

with open(sys.argv[1]) as f:
    grid = f.read()

grid = grid.split()
grid_list = [list(g) for g in list(grid)]


def roll_accesible(grid, x, y):
    if grid[x][y] != "@":
        return 0, grid[x][y]
    rows = len(grid)
    cols = len(grid[0])
    count = -1
    for r in range(max(0, x - 1), min(rows, x + 2)):
        for c in range(max(0, y - 1), min(cols, y + 2)):
            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] == "@":
                    count += 1
                    if count > 3:
                        return 0, "@"

    return 1, "X"


result = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        result.append(roll_accesible(grid, r, c)[0])

print(f"Part 1: {sum(result)}")

result = []
new_grid = deepcopy(grid_list)
while True:
    for r in range(len(grid_list)):
        for c in range(len(grid_list[0])):
            val, symbol = roll_accesible(grid_list, r, c)
            grid_list[r][c] = symbol
            result.append(val)
    if new_grid == grid_list:
        break
    new_grid = deepcopy(grid_list)

print(f"Part 2: {sum(result)}")
