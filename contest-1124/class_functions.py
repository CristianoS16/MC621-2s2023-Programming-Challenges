import math


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


# Outra maneira de calcular o produto cruzado escalar
# Nota: Para aceitar pontos colineares, precisamos mudar o > 0
# Retorna True se o ponto está do lado esquerdo da linha pq
def ccw(p, q, r):
    return cross((q[0] - p[0], q[1] - p[1]), (r[0] - p[0], r[1] - p[1])) > 0


def angle(p1, p2, p3):
    def angle_from_origin(x, y):
        return math.atan2(y, x)

    vector1 = (p1[0] - p2[0], p1[1] - p2[1])
    vector2 = (p3[0] - p2[0], p3[1] - p2[1])

    angle1 = angle_from_origin(*vector1)
    angle2 = angle_from_origin(*vector2)

    angle = angle2 - angle1

    # Normalize the angle to be between 0 and 2*pi
    angle = (angle + 2 * math.pi) % (2 * math.pi)

    return angle


def inPolygon(pt, P):
    if len(P) == 0:
        return False
    total_sum = 0
    for i in range(0, len(P) - 1):
        if ccw(pt, P[i], P[i + 1]):
            total_sum += angle(P[i], pt, P[i + 1])
        else:
            total_sum -= angle(P[i], pt, P[i + 1])

    print(total_sum)
    return abs(abs(total_sum) - 2 * math.pi) < 1e-9


polygon_convex = [(0, 0), (0, 5), (5, 5), (5, 0)]
point1 = (2, 2)
point2 = (3, 4)
print(inPolygon(point1, polygon_convex))
