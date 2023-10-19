import re

# Assemble a dictionary using as key the number of fibonacci and as value your position
FIBONACCI_NUMBER_LIMIT = 2 ** 31
fib_idx = {
    1: 1,
    2: 2
}
current_last_fib = 1
current_fib = 2
current_idx = 2
while current_fib < FIBONACCI_NUMBER_LIMIT:
    aux_last_fib = current_last_fib
    current_last_fib = current_fib
    current_fib += aux_last_fib

    current_idx += 1
    fib_idx[current_fib] = current_idx


tests_number = int(input())
while(tests_number):
    tests_number -= 1

    fib_numbers_len = int(input())
    fib_numbers = [int(n) for n in input().split()]
    # Remove unnecessary characters of the input
    cipher_valid_phrase = re.findall(r'[A-Z]', input())
    # Determines the size of the output based on the largest number of fibonacci given
    decoded_phrase = [' '] * fib_idx[max(fib_numbers)]

    for letter_idx in range(fib_numbers_len):
        # Reorders the letters using the dictionary with the numbers of Fibonacci and the positions
        decoded_phrase[fib_idx[fib_numbers[letter_idx]] -
                       1] = cipher_valid_phrase[letter_idx]

    print(''.join(decoded_phrase))
