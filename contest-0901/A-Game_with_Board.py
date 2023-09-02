tests_number = int(input())

while(tests_number):
    tests_number -= 1

    n = int(input())

    # To 5 or more numbers there is a combination in which Alice leaves
    # only two numbers 1's to Bob after sum a number greater than 2
    # So she guarantees victory
    if(n >= 5):
        print("Alice")
    else:
        print("Bob")
