import math


def get_x_projection(vet_len, angle):
    return vet_len * math.cos(math.radians(angle))


def get_y_projection(vet_len, angle):
    return vet_len * math.sin(math.radians(angle))


tests_number = int(input())
while tests_number:
    tests_number -= 1

    commands_number = int(input())

    x_point = 0
    y_point = 0
    current_degree = 0
    degree_1 = 0
    degree_2 = 0

    polygon_size = 0
    for i in range(commands_number):
        command, number = input().split()
        if number == "?":
            lost_command = command
            lost_degree = current_degree
        else:
            number = int(number)

            if command == "fd":
                polygon_size += 1
                x_point += get_x_projection(number, current_degree)
                y_point += get_y_projection(number, current_degree)
            elif command == "bk":
                polygon_size += 1
                x_point -= get_x_projection(number, current_degree)
                y_point -= get_y_projection(number, current_degree)
            elif command == "lt":
                degree_1 += number
                degree_2 += 180 - number
                current_degree += number
            elif command == "rt":
                degree_1 += 180 - number
                degree_2 += number
                current_degree -= number

    if lost_command == "fd" or lost_command == "bk":
        print(round(math.sqrt(x_point**2 + y_point**2)))
    else:
        if round(math.sqrt(x_point**2 + y_point**2)) == 0:
            print(0)
        else:
            # elif polygon_size > 2:
            #     internal_angle = (polygon_size - 2) * 180

            #     # print("internal_angle", internal_angle)
            #     # print("degree_1", degree_1)
            #     # print("degree_2", degree_2)

            #     internal_option = internal_angle - degree_1
            #     internal_option2 = internal_angle - degree_2
            #     # print("internal_option", internal_option)
            #     # print("internal_option2", internal_option2)

            #     if degree_2 + 360 - internal_option == 360:
            #         # print("degree_1 interno")
            #         # print((360 - degree_2) // 2)
            #     # else:
            #         # print("degree_2 interno")
            #         # print((360 - degree_1) // 2)
            # else:
            # print("banban")

            print("final --> ", lost_command, 360 - (current_degree % 360))
# 5
# fd 100
# lt 120
# fd 100
# rt ?
# fd 100


# 6
# fd 3
# rt 90
# fd 4
# rt 90
# rt ?
# fd 5
