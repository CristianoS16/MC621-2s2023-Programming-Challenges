n = int(input())
routers_idx = [int(n) for n in input().split()]

result = [n]
current_idx = n - 1

# Travel the set of routers using the indicated indices
while current_idx != 0 and 1 != routers_idx[current_idx-1]:
    result.append(routers_idx[current_idx-1])
    current_idx = routers_idx[current_idx-1]-1
result.append(routers_idx[current_idx-1])

print(*result[::-1])
