tests_number = int(input())
while(tests_number):
    tests_number -= 1

    str1 = input()
    str2 = input()

    set1 = set(str1)
    set2 = set(str2)

    # If there is at least one letter in common it is possible to turn one string into the other
    if len(set1.intersection(set2)) > 0:
        print("YES")
    else:
        print("NO")
