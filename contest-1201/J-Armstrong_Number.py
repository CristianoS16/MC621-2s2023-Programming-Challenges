tests_number = int(input())

while tests_number:
    tests_number -= 1

    aux_n = input()
    n = int(aux_n)

    digits = []
    for digit in aux_n:
        digits.append(int(digit))

    total_sum = 0
    i = 0
    while total_sum < n:
        total_sum = sum([digit**i for digit in digits])
        i += 1

    if total_sum == n:
        print("Armstrong")
    else:
        print("Not Armstrong")
