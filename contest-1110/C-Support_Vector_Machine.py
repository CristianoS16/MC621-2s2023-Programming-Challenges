import math
from sys import stdin


def get_distance(n, ws, xs, b):
    wx_sum = sum([w * x for w, x in zip(ws, xs)])
    ww_sum = sum([w**2 for w in ws])

    return (wx_sum + b) / math.sqrt(ww_sum)

n = int(input())
ws = [float(i) for i in input().split()]
b = ws.pop(n)

for line in stdin:
    xs = [float(i) for i in line.split()]
    print(round(get_distance(n, ws, xs, b), 5))
