# I used  chatGPT to do the function to tell the subsequent number

def count_subsequences(string, pattern):
    string_len = len(string)
    pattern_len = len(pattern)

    # Initialize a matrix to store the number of correspondences
    dp = [0] * (pattern_len + 1)

    # Initialize the first position with 1 as there is an empty subsequence in any string.
    dp[0] = 1

    for i in range(1, string_len + 1):
        prev = 1  # Stores the previous value dp[i-1][j-1]
        for j in range(1, pattern_len + 1):
            temp = dp[j]  # Stores the previous value dp[i-1][j]
            if string[i - 1] == pattern[j - 1]:
                dp[j] += prev
            prev = temp

    return dp[pattern_len]


string = input()
new_string = ''
count_vs = 0

# Creates a new string replacing v's with w's
for c in string:
    if c == 'v':
        count_vs += 1
    else:
        if count_vs != 0:
            new_string += 'w'*(count_vs-1)
            count_vs = 0
        new_string += 'o'
if count_vs != 0:
    new_string += 'w'*(count_vs-1)

print(count_subsequences(new_string, "wow"))
