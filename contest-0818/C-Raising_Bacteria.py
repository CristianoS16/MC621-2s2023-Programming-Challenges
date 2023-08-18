desired_number = int(input())

"""
Bacteria always double, so to know the amount required to view 
the desired number just break the number in power of 2,
which corresponds to binary representation
"""
print(bin(desired_number).count("1"))
