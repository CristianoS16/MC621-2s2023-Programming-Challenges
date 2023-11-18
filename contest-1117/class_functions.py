def inside_circle(point_p, point_c, radius):
    # all integer version
    dx = point_p[0] - point_c[0]
    dy = point_p[1] - point_c[1]

    Euc = dx * dx + dy * dy
    rSq = radius * radius  # all integer

    return 0 if Euc < rSq else 1 if Euc == rSq else 2


import math


def area(ab, bc, ca):
    s = (ab + bc + ca) / 2
    return math.sqrt(s * (s - ab) * (s - bc) * (s - ca))


def perimeter(ab, bc, ca):
    return ab + bc + ca


def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def r_in_circle(ab, bc, ca):
    return area(ab, bc, ca) / (0.5 * perimeter(ab, bc, ca))


def r_in_circle_points(point_a, point_b, point_c):
    return r_in_circle(
        dist(point_a, point_b), dist(point_b, point_c), dist(point_c, point_a)
    )
