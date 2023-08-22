n = int(input())
m = int(input())

# The rest can be obtained with the bits to the right of the bit in the position len(bin(m))-n
# Creates a mask with n bits linked to extract the bits responsible for the rest
mask = (1 << n) - 1
result = m & mask

print(result)
