balls_1, balls_2, remove_balls_limit_1, remove_balls_limit_2 = map(int, input().split())

if balls_1 < balls_2:
    print("Second")
elif balls_1 > balls_2:
    print("First")
else:
    print("Second")
