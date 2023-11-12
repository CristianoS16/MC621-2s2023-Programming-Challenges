import math

EPS = 1e-7
LIGHT_RADIUS = 8

tests_number = int(input())
while tests_number:
    tests_number -= 1

    book_point = [float(n) for n in input().split()]

    candles_amount = int(input())
    candles_points = []
    output = "curse the darkness"

    for i in range(candles_amount):
        current_candle = [float(n) for n in input().split()]
        if (
            output == "curse the darkness"
            and math.hypot(
                book_point[0] - current_candle[0], book_point[1] - current_candle[1]
            )
            < LIGHT_RADIUS
        ):
            output = "light a candle"

    print(output)
