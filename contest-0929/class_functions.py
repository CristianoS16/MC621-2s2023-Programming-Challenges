def floydCycleFinding(x0, func):
    # 1st part
    tortoise = func(x0)
    hare = func(func(x0))
    while tortoise != hare:
        tortoise = func(tortoise)
        hare = func(func(hare))
    # 2nd part
    mu = 0
    hare = x0
    while tortoise != hare:
        tortoise = func(tortoise)
        hare = func(hare)
        mu += 1
    # 3rd part
    cycle_len = 1
    hare = func(tortoise)
    while tortoise != hare:
        hare = func(hare)
        cycle_len += 1

    return mu, cycle_len


# print(floydCycleFinding(7, lambda x: (7*x+5) % 12))
print(floydCycleFinding(1, lambda x: x**x % 10))
