# Definition of the given function
def f(n):
    if n == 0:
        return 2**0.5 + 3**0.5+6**0.5
    else:
        return (f(n-1)**2 - 5)/(2*f(n-1)+4)


# After the third interaction there is a cycle of length 2
# for i in range(10):
#     print("{} --> {:.10f}".format(i, f(i)))
# 0 --> 5.5957541127
# 1 --> 1.7320508076
# 2 --> -0.2679491924
# 3 --> -1.4226497308
# 4 --> -2.5773502692
# 5 --> -1.4226497308
# 6 --> -2.5773502692
# 7 --> -1.4226497308
# 8 --> -2.5773502692
# 9 --> -1.4226497308

# Stores known results in a list
f_results = ["{:.10f}".format(f(i)) for i in range(5)]
while True:
    try:
        n = int(input())
        # Uses known results to determine the value of f (n)
        if n < 5:
            print(f_results[n])
        elif n % 2 == 0:
            print(f_results[4])
        else:
            print(f_results[3])

    except EOFError:
        break
