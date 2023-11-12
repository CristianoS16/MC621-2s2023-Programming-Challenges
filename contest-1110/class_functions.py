import math

EPS = 1e-9


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = x, y

    def __str__(self):
        return f"Point: ({self.x}, {self.y})"

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other):
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS

    @staticmethod
    def dist(point_1, point_2):
        return math.hypot(point_1.x - point_2.x, point_1.y - point_2.y)

    @staticmethod
    def DEG_to_RAD(degrees):
        return degrees * math.pi / 180.0

    @staticmethod
    def rotate(point, theta):
        rad = Point.DEG_to_RAD(theta)
        return Point(
            point.x * math.cos(rad) - point.y * math.sin(rad),
            point.x * math.sin(rad) + point.y * math.cos(rad),
        )


# point1 = Point(3.0, 0.0)
# point2 = Point(0.0, 4.0)
# print(point1.dist(point1))


class Line:
    def __init__(self, a=0.0, b=0.0, c=0.0):
        self.a, self.b, self.c = a, b, c

    def __str__(self):
        return f"Line: {self.a}x + {self.b}y + {self.c} = 0"

    @staticmethod
    def are_parallel(line_1, line_2):
        return abs(line_1.a - line_2.a) < EPS and abs(line_1.b - line_2.b) < EPS

    @staticmethod
    def are_same(line_1, line_2):
        return line_1.are_parallel(line_2) and abs(line_1.c - line_2.c) < EPS

    @staticmethod
    def are_intersect(line_1, line_2):
        if line_1.are_parallel(line_2):
            return False, None  # No intersection for parallel lines

        denominator = line_1.a * line_2.b - line_2.a * line_1.b
        x = (line_2.b * line_1.c - line_1.b * line_2.c) / denominator

        if abs(line_1.b) > EPS:
            y = -(line_1.a * x + line_1.c)
        else:
            y = -(line_2.a * x + line_2.c)

        return True, Point(x, y)

    @staticmethod
    def points_to_line(p1, p2):
        line = Line()

        if abs(p1.x - p2.x) < EPS:
            line.a = 1.0
            line.b = 0.0
            line.c = -p1.x
        else:
            line.a = -(p1.y - p2.y) / (p1.x - p2.x)
            line.b = 1.0
            line.c = -(line.a * p1.x) - p1.y

        return line


print(Line.points_to_line(Point(-6, -1), Point(6, -4)))
