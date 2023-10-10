tests_number = int(input())

while(tests_number):
    tests_number -= 1

    binary_number_len = int(input())
    binary_number = input()

    if binary_number_len == 0:
        print(0)
    else:

        # Defines the Index to travel the string given
        left_idx = 0
        right_idx = binary_number_len-1

        # Travel strings from the extremes to the center until you find a position where the currents extremos are equals
        while(binary_number[left_idx] != binary_number[right_idx] and left_idx < right_idx):
            left_idx += 1
            right_idx -= 1

        print(right_idx - left_idx + 1)
