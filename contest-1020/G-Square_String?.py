tests_number = int(input())
while(tests_number):
    tests_number -= 1

    string = input()
    string_len = len(string)

    if string_len % 2 == 1:
        print("NO")

    else:
        if string[:string_len//2] == string[string_len//2:]:
            print("YES")
        else:
            print("NO")
