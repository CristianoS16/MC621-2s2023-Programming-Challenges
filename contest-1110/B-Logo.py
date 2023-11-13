import math


def get_x_projection(vet_len, angle):
    return vet_len * math.cos(angle)


def get_y_projection(vet_len, angle):
    return vet_len * math.sin((angle))


tests_number = int(input())
while tests_number:
    tests_number -= 1

    commands_number = int(input())

    x_point = 0
    y_point = 0
    current_degree = 0

    for i in range(commands_number):
        command, number = input().split()
        number = int(number)

        if command == "fd":
            x_point += get_x_projection(number, current_degree)
            y_point += get_y_projection(number, current_degree)
        elif command == "bk":
            x_point -= get_x_projection(number, current_degree)
            y_point -= get_y_projection(number, current_degree)
        elif command == "lt":
            current_degree += math.radians(number)
        elif command == "rt":
            current_degree -= math.radians(number)

    print(round(math.sqrt(x_point**2 + y_point**2)))
