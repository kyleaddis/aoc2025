import sys

if len(sys.argv) != 2:
    sys.exit(1)
grid = ""

with open(sys.argv[1]) as f:
    grid = f.read()

grid = grid.split()


def roll_accesible(grid, x, y):
    if grid[x][y] != "@":
        return 0
    rows = len(grid)
    cols = len(grid[0])
    count = -1
    for r in range(max(0, x - 1), min(rows, x + 2)):
        for c in range(max(0, y - 1), min(cols, y + 2)):
            if 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] == "@":
                    count += 1
                    if count > 3:
                        return 0

    return 1


result = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        result.append(roll_accesible(grid, r, c))

print(sum(result))
