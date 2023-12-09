a = input()
b = input()

a_4 = 0
a_7 = 0
for i in range(len(a)):
    if a[i] != b[i]:
        if a[i] == "4":
            a_7 += 1
        else:
            a_4 += 1

print(max(a_4, a_7))
