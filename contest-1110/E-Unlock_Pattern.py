import math

coords = {}

for i in range(3):
    n1, n2, n3 = map(int, input().split())

    coords[n1] = [0, i]
    coords[n2] = [1, i]
    coords[n3] = [2, i]

total_dist = 0
for n in range(1, 9):
    total_dist += math.hypot(
        coords[n][0] - coords[n + 1][0], coords[n][1] - coords[n + 1][1]
    )
print(total_dist)
