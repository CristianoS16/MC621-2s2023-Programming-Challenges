tests_number = int(input())
while(tests_number):
    tests_number -= 1

    string = input()
    separador = 0

    for i in range(len(string)):
        if string[i] in string[i+1:]:
            separador += 1
        else:
            break
    print(string[separador:])
