string = input()

count_4 = string.count("4")
count_7 = string.count("7")

if count_4 == 0 and count_7 == 0:
    print(-1)
elif count_7 > count_4:
    print(7)
else:
    print(4)
