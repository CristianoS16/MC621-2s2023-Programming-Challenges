while True:
    brownie_amount = int(input())
    if brownie_amount == 0:
        break

    stans_score = 0
    ollie_score = 0
    coords = []

    for _ in range(brownie_amount):
        coords.append([*map(int, input().split())])

    x_threshold, y_threshold = coords.pop(brownie_amount // 2)
    for brownie_x, brownie_y in coords:
        if brownie_x == x_threshold or brownie_y == y_threshold:
            continue

        if (brownie_x > x_threshold and brownie_y > y_threshold) or (
            brownie_x < x_threshold and brownie_y < y_threshold
        ):
            stans_score += 1
        else:
            ollie_score += 1

    print(f"{stans_score} {ollie_score}")
