while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    output = "wrong"
    if a >= b and a >= c:
        if a**2 == b**2 + c**2:
            output = "right"
    elif b >= a and b >= c:
        if b**2 == a**2 + c**2:
            output = "right"
    elif c >= a and c >= b:
        if c**2 == a**2 + b**2:
            output = "right"

    print(output)
