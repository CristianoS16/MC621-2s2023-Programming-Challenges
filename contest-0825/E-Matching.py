tests_number = int(input())

while(tests_number):
    tests_number -= 1

    s = input()
    total = 0

    # If the string starts with 0 the result is zero by default
    if s[0] == '0':
        print(total)
        continue

    # For each "?", that is not at the beginning of the string, there are 10 possibilities
    question_number = s[1:].count('?')
    total = 10**question_number

    # If there is a "?" at the beginning of the string there are only 9 possibilities for it
    if s[0] == '?':
        total = 9*total

    print(total)
