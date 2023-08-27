count = 0

while(1):
    count += 1

    n, f = map(int, input().split())
    if (n == 0 and f == 0):
        break

    total = 0
    for i in range(n):
        total += int(input())
    print(
        f"Bill #{count} costs {total}: each friend should pay {total//f}\n")
