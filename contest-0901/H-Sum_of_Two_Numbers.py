# I read part of the problem tip
tests_number = int(input())


def sum_digits(number):
    count = 0
    while number > 0:
        digit = number % 10
        count += digit
        number //= 10
    return count


while(tests_number):
    tests_number -= 1

    n = int(input())

    # If the number is even the sum of its half is equal to it
    # and the difference between them and less or equal to 1
    if (n % 2 == 0):
        print(f"{int(n/2)} {int(n/2)}")

    else:
        floor = int((n-1)/2)
        ceil = int((n+1)/2)

        # If the number is odd and the condition is not satisfied, so is necessary some ajusts
        if abs(sum_digits(ceil) - sum_digits(floor)) > 1:
            floor = 0
            ceil = 0
            i = 0
            change = True
            while n > 0:
                digit = n % 10
                if digit % 2 == 0:
                    floor += digit/2*10**i
                    ceil += digit/2*10**i
                else:
                    if change:
                        floor += (digit-1)/2*10**i
                        ceil += (digit+1)/2*10**i
                        change = False
                    else:
                        ceil += (digit-1)/2*10**i
                        floor += (digit+1)/2*10**i
                        change = True
                i += 1
                n //= 10

        print(f"{int(floor)} {int(ceil)}")
