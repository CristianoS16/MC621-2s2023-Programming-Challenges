import math


def get_x_projection(vet_len, angle):
    return vet_len * math.cos(math.radians(angle))


def get_y_projection(vet_len, angle):
    return vet_len * math.sin(math.radians(angle))


def update_positions(command, number, x_point, y_point, current_degree):
    if command == "fd":
        x_point += get_x_projection(number, current_degree)
        y_point += get_y_projection(number, current_degree)
    elif command == "bk":
        x_point -= get_x_projection(number, current_degree)
        y_point -= get_y_projection(number, current_degree)
    elif command == "lt":
        current_degree += number
    elif command == "rt":
        current_degree -= number

    return x_point, y_point, current_degree


tests_number = int(input())
while tests_number:
    tests_number -= 1

    commands_number = int(input())

    x_point = 0
    y_point = 0
    current_degree = 0

    after_lost_commands = []
    is_after_lost_command = False

    for i in range(commands_number):
        command, number = input().split()
        if is_after_lost_command:
            after_lost_commands.append((command, number))
        if number == "?":
            is_after_lost_command = True
            lost_command = command
            lost_degree = current_degree
            x_lost = x_point
            y_lost = y_point
        else:
            x_point, y_point, current_degree = update_positions(
                command, int(number), x_point, y_point, current_degree
            )

    # If the lost command is to move uses the distance of the previous problem
    if lost_command == "fd" or lost_command == "bk":
        print(round(math.sqrt(x_point**2 + y_point**2)))
    # If the lost command is to rotate, the 360 options are tested,
    # from the point where the command was lost
    else:
        for number in range(0, 360):
            x_point, y_point, current_degree = update_positions(
                lost_command, number, x_lost, y_lost, lost_degree
            )
            for i in range(len(after_lost_commands)):
                x_point, y_point, current_degree = update_positions(
                    after_lost_commands[i][0],
                    int(after_lost_commands[i][1]),
                    x_point,
                    y_point,
                    current_degree,
                )

            if round(math.sqrt(x_point**2 + y_point**2)) == 0:
                break
        print(number)
