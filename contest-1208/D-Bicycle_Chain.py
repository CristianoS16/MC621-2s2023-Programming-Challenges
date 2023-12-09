pedal_stars = int(input())
a = [int(n) for n in input().split()]
wheel_stars = int(input())
b = [int(n) for n in input().split()]

ratio = {}

for i in range(pedal_stars):
    for j in range(wheel_stars):
        if b[j] % a[i] == 0:
            if b[j] / a[i] in ratio.keys():
                ratio[b[j] / a[i]] += 1
            else:
                ratio[b[j] / a[i]] = 1

print(ratio[max(ratio.keys())])
