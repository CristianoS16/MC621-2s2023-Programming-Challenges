tests_number = int(input())

# Uses multipulation of Modular Arithmetica view in class
def mult_rest(x, y, n):
    return((x % n)*(y % n)) % n

# Uses addition of Modular Arithmetica view in class
def add_rest(x, y, n):
    return((x % n)+(y % n)) % n


while(tests_number):
    tests_number -= 1

    friends_qty, boxes_qty = map(int, input().split())
    final_result = 0

    for i in range(boxes_qty):
        boxes_config = [int(n) for n in input().split()]
        box_result = boxes_config[1]
        # Travel the content of each box to find the number of remaining chocolates
        for box_conf in boxes_config[2:]:
            box_result = mult_rest(box_result, box_conf, friends_qty)

        # Accumulates the number of remaining chocolates of all boxes
        final_result = add_rest(final_result, box_result, friends_qty)

    print(final_result)
