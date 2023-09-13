# I use chatGPT to understant the problem and build the follow function

# I used chatGPT to generate this function that makes a combination of k elements in a space with n elements
def combination(n, k):
    if k < 0 or k > n:
        return 0

    # Initiatize the matrix to the Easter triangle
    C = [[0] * (k + 1) for _ in range(n + 1)]

    # Fill the first column with 1s
    for i in range(n + 1):
        C[i][0] = 1

    # Use the form C(n, k) = C(n-1, k-1) + C(n-1, k)
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]


tests_number = int(input())

while(tests_number):
    tests_number -= 1
    number_of_wins = int(input())
    prob_A_win = float(input())

    final_prob = 0
    for i in range(number_of_wins):
        """
        Apply probability mass function of binomial distribution to solve the problem
        https://en.wikipedia.org/wiki/Binomial_distribution
        """
        final_prob += combination(number_of_wins+i-1, i) * \
            prob_A_win**number_of_wins * (1-prob_A_win)**i

    print("{:.2f}".format(final_prob))
