import sys

if len(sys.argv) != 2:
    sys.exit(1)
codes = ""

with open(sys.argv[1]) as f:
    codes = f.read()

zeros = 0
current = 50
for c in codes.split():
    d = c[0]
    v = int(c[1::]) % 100

    if d == "L":
        v *= -1

    n = current + v
    print(f"pre: {d}, {v}, {current}, {n}")
    if n < 0:
        n = 100 + n
    if n > 100:
        n = n - 100
    if n == 100:
        n = 0
    print(f"post: {n}")
    current = n
    if n == 0:
        zeros += 1

print(zeros)
