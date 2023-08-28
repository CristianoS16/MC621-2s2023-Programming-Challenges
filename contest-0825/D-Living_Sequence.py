# I used chat GPT help

# Convert a decimal number to base 9, return a string
def get_nine_base(num):
    nine_base_num = []
    while num > 9:
        nine_base_num.append(str(num % 9))
        num = num // 9
    nine_base_num.append(str(num))
    return ''.join(nine_base_num[::-1])


tests_number = int(input())

while(tests_number):
    tests_number -= 1

    position = int(input())

    # The numbers are converted to base 9 because without the number four
    # there are only 9 possibilities: 1, 2, 3, 5, 6, 7, 8, 9 and 0
    aux_num_str = get_nine_base(position)
    final_number = ''

    # as we are removing the number four, all base 9 values smaller than 4 are valid
    # Values equal to or greater than four must be adjusted, adding one unit
    for num in aux_num_str:
        if num >= '4':
            final_number += str(int(num) + 1)
        else:
            final_number += num

    print(final_number)
