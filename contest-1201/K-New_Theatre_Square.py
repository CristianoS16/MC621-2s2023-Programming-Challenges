tests_number = int(input())

while tests_number:
    tests_number -= 1

    n, m, price_1_1, price_1_2 = map(int, input().split())
    use_only_1_1 = price_1_2 > 2 * price_1_1
    total_1_1 = 0
    total_1_2 = 0

    for i in range(n):
        line = input()
        if use_only_1_1:
            total_1_1 += line.count(".")
        else:
            j = 0
            while j < m:
                if line[j] == ".":
                    if j + 1 < m and line[j + 1] == ".":
                        total_1_2 += 1
                        j += 2
                    else:
                        total_1_1 += 1
                        j += 1
                else:
                    j += 1

    print(total_1_1 * price_1_1 + total_1_2 * price_1_2)
