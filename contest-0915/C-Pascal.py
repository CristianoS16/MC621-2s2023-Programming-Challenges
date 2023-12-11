# I used chatGPT to find a way to test fewer numbers to find the smallest whole divider of a number
def get_smallest_div(n):
    for smallest_div in range(2, int(n**0.5) + 1):
        if(n % smallest_div == 0):
            return smallest_div
    return 1

n = int(input())
smallest_div = get_smallest_div(n)

# If the number is prime then it will perish all numbers until it reaches the 1
if smallest_div == 1:
    print(n-1)
else:
    # n//smallest_div corresponds to the largest entire divisor of n and
    # the first number found as exit of the given code
    print(n-n//smallest_div)
