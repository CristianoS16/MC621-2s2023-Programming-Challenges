square_side_lenght, point_x, point_y = map(int, input().split())

if 0 < point_x < square_side_lenght and 0 < point_y < square_side_lenght:
    print(0)
elif (
    0 > point_x
    or 0 > point_y
    or point_x > square_side_lenght
    or point_y > square_side_lenght
):
    print(2)
else:
    print(1)
