# I read part of the problem tip
import math

n = int(input())

# Uses the circular permutation formula as a base and checks the number of permutation for the whole set
# Then divide by the amount of people they should have in each group
print(math.factorial(n - 1)//(n//2))
