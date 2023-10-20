# Levenshtein distance algorithm as showed in the class
def levenshtein_distance(seq1, seq2):
    n = len(seq1)+1
    m = len(seq2)+1

    # Build table
    table = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        table[i][0] = i
    for j in range(1, m):
        table[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            # check for match, mismatch or gap
            value = 0 if seq1[i-1] == seq2[j-1] else 1
            table[i][j] = min(
                table[i-1][j-1] + value,
                table[i-1][j] + 1,
                table[i][j-1] + 1)

    return table[n-1][m-1]


tests_number = int(input())
while(tests_number):
    tests_number -= 1

    string1 = input()
    string2 = input()

    print(levenshtein_distance(string1, string2))
