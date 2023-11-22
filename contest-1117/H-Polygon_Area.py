# http://www.dinamatica.com.br/2011/04/area-de-poligonos-atraves-de.html
while True:
    vertices_len = int(input())

    if vertices_len == 0:
        break

    last_x, last_y = map(int, input().split())
    first_x, first_y = last_x, last_y
    area = 0

    for _ in range(vertices_len - 1):
        current_x, current_y = map(int, input().split())
        area += (last_x * current_y) - (last_y * current_x)

        last_x, last_y = current_x, current_y

    area += (last_x * first_y) - (last_y * first_x)

    print(f"CCW {area/2}" if area > 0 else f"CW {-area/2}")
