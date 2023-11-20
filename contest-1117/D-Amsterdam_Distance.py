import math

segments_number, half_rings_number, city_radius = map(float, input().split())
ax, ay, bx, by = map(int, input().split())

angle = math.pi / segments_number
rings_height = city_radius / half_rings_number

linear_dist = abs(by - ay) * rings_height
arc_dist = rings_height * min(ay, by) * (angle * abs(ax - bx))

# Check whether it is closer to walk along the arcs of the circle or just along the radius
total_dist = min(arc_dist + linear_dist, rings_height * (ay + by))
print(round(total_dist, 7))
