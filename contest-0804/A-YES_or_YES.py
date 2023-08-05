valid_strings = ["Yes", "YeS", "YEs", "YES", "yEs", "yES", "yeS", "yes"]

test_number = int(input())
while(test_number):
    current_string = input()
    if(current_string in valid_strings):
        print("YES")
    else:
        print('NO')
    test_number -= 1
