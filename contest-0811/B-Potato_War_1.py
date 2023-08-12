x1, y1, x2, y2 = map(int, input().split())

# When y1 <= y2 it is only possible that technoblade wins 1st Potato War if it starts with more potatoes
if y1 <= y2:
    if x2 >= x1:
        print(-1)
    else:
        print(0)
else:
    # Solving the inequation X1+Days*Y1 > X2+Days*Y2 the number of days can be obtained as days = (x2-x1)/(Y1-Y2)
    days = int((x2-x1)/(y1-y2))
    if x1+days*y1 > x2+days*y2:
        print(max(days, 0))
    else:
        print(max(days+1, 0))
