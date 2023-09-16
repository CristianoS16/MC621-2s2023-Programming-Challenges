# Calcula the GCD
def get_gcd(number_1, number_2):
    while(number_2 != 0):
        rest = number_1 % number_2
        number_1 = number_2
        number_2 = rest

    return number_1


ring_number = int(input())
rings_ratio = [int(n) for n in input().split()]

for i in range(1, ring_number):
    gcd = get_gcd(rings_ratio[i], rings_ratio[0])
    # Shows the simplified fraction
    print(f"{rings_ratio[0]//gcd}/{rings_ratio[i]//gcd}")
