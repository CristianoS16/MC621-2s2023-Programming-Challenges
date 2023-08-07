tests_number = int(input())

while(tests_number):
    tests_number -= 1
    n = int(input())
    original_array = input().replace(" ", "")

    # Only one number is a non-decreasing sequence, no operations required
    if n == 1:
        print(0)
    else:

        zeros_amount = original_array.count("0")
        ones_array = original_array.split("0")
        operations = 0

        """
        With each set of ones accounting for operations to remove them and remove the zeros ahead.
        Zero sets are taken into account and discounted
        When there are no more groups of 1 to remove accounting for the necessary
        operations to remove the remaining zeros
        """
        for i in range(len(ones_array)):
            ones_group = len(ones_array[i])
            if zeros_amount >= ones_group:
                operations += ones_group
                zeros_amount -= ones_group
            else:
                operations += zeros_amount
                break
            if(zeros_amount > 0):
                zeros_amount -= 1

        print(operations)
