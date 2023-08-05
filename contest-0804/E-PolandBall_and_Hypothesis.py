def is_prime(number):
    if number < 2:
        False
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True


n = int(input())

for m in range(1, 1000):
    if not is_prime(n*m+1):
        print(m)
        break
