permutation_size = int(input())

if permutation_size % 2 == 1:
    print(-1)
else:
    print(*[i for i in range(permutation_size, 0, -1)])
