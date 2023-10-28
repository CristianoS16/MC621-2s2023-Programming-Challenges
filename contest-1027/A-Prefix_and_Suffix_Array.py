tests_number = int(input())
while(tests_number):
    tests_number -= 1

    string_len = int(input())
    prefix_suffix_list = input().split()
    select_strings = []

    for string in prefix_suffix_list:
        if(len(string) == string_len-1):
            select_strings.append(string)

    if string_len < 3 and select_strings[0] == select_strings[1]:
        print("YES")
    else:
        if select_strings[0][1:] == select_strings[1][:-1]:
            complete_string = select_strings[0]+select_strings[1][-1]
        else:
            complete_string = select_strings[1]+select_strings[0][-1]

        if(complete_string == complete_string[::-1]):
            print("YES")
        else:
            print("NO")
