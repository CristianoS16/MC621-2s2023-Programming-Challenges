tests_number = int(input())

while(tests_number):
    tests_number -= 1

    line = input()

    # Check the beginning of the sentence and when a match occurs print the rest of the sentense
    if line.lower()[0:10] == "simon says":
        print(line[10:])
