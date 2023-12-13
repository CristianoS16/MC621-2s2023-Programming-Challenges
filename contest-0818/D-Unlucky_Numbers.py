def get_luckiness(number):
    max_digit = 0
    min_digit = 9

    while number > 0:
        digito = number % 10  # Obtém o último dígito
        if digito > max_digit:
            max_digit = digito
        if digito < min_digit:
            min_digit = digito
        number //= 10

    return max_digit - min_digit


tests_number = int(input())

while(tests_number):
    tests_number -= 1

    l, r = input().split()

    # If there is only one number in the sequence then it must be luckiness
    if l == r:
        ans = l
    # If the order of grandeur of the numbers of sequence changes,
    # then there must be a number with luckiness equal to zero and all the digits equal to 9
    elif(len(l) < len(r)):
        ans = '9' * len(l)
    # If contrary to all numbers are tested
    else:
        # Stir equally two numbers
        for i in range(len(l)):
            if l[i] != r[i]:
                prefix = l[:i]
                l = l[i:]
                r = r[i:]
                break

        l_int = int(l)
        r_int = int(r)
        min_luckiness = 9

        for i in range(l_int, r_int+1):
            current_luckiness = get_luckiness(i)
            if min_luckiness > current_luckiness:
                ans = i
                min_luckiness = current_luckiness
            if min_luckiness == 0:
                break

        ans = prefix + ans

    print(ans)
