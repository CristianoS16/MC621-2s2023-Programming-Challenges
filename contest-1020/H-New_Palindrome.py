tests_number = int(input())
while(tests_number):
    tests_number -= 1

    string = input()

    string_len = len(string)
    string_set = set(string)

    char_counts = {}

    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    if len(string_set) > 2 or (len(string_set) == 2 and min(char_counts.values()) > 1):
        print("YES")
    else:
        print("NO")
