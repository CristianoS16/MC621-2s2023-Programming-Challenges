# I use ChatCGPT help
sticks_number = int(input())
sticks_size = [int(n) for n in input().split()]
sticks_size.sort()
output = "impossible"
for i in range(sticks_number - 2):
    if sticks_size[i] + sticks_size[i + 1] > sticks_size[i + 2]:
        output = "possible"

print(output)
