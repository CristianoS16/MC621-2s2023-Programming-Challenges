import math

while True:
    r, total_points, total_points_inside = map(float, input().split())

    if r == total_points_inside == total_points == 0:
        break

    cicle_area = math.pi * r**2
    area_points = (int(total_points_inside) / int(total_points)) * (2 * r) ** 2

    print(f"{round(cicle_area, 6)} {round(area_points, 6)}")
