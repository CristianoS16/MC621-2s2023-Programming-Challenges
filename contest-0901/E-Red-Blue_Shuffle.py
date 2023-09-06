tests_number = int(input())

while(tests_number):
    tests_number -= 1

    cards_number = int(input())
    red_digits = input()
    blue_digits = input()

    """
    As always there are two numbers on the same card, 
    the largest number will give advantage to the competitor of that color.
    That way just check the cards individually and see which 
    competitor has the most advantage in the end.
    """
    red_count = 0
    blue_count = 0
    for i in range(cards_number):
        if(red_digits[i] > blue_digits[i]):
            red_count += 1
        elif(blue_digits[i] > red_digits[i]):
            blue_count += 1

    if(red_count > blue_count):
        print("RED")
    elif(blue_count > red_count):
        print("BLUE")
    else:
        print("EQUAL")
