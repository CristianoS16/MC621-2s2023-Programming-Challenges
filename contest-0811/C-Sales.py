n, k = map(int, input().split())
sales = [int(n) for n in input().split()]

# Defines the initial state
current_sum = sum(sales[:k])
max_sum = min_sum = current_sum
max_idx = min_idx = 0

for i in range(1, n-k+1):
    # If Sales [i+k-1] == Sales [i-1] current_sum does not change
    if sales[i+k-1] == sales[i-1]:
        continue
    # Calculate the new current_sum by adding the value of the new element
    # and removing the value of the element that is no longer in the interval
    current_sum += sales[i+k-1] - sales[i-1]
    # Update the indices
    if current_sum > max_sum:
        max_sum = current_sum
        max_idx = i
    if current_sum < min_sum:
        min_sum = current_sum
        min_idx = i

print(min_idx + 1, max_idx + 1)
