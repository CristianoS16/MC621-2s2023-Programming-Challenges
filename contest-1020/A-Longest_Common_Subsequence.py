from sys import stdin


# Needleman Wunsnch’s algorithm as showed in the class
def needleman_wunsnchs(seq1, seq2, match=2, mismatch=-1, gap=-1):

    rows = len(seq1) + 1
    columns = len(seq2) + 1

    # Build table
    table = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(1, rows):
        table[i][0] = i * gap
    for j in range(1, columns):
        table[0][j] = j * gap

    for i in range(1, rows):
        for j in range(1, columns):
            # check for match, mismatch or gap
            value = match if seq1[i-1] == seq2[j-1] else mismatch
            table[i][j] = max(
                table[i-1][j-1] + value,
                table[i-1][j] + gap,
                table[i][j-1] + gap)

    return table[rows-1][columns-1]


# Uses the Needleman Wunsnch's algorithm to find the longest common sequence
for str1, str2 in zip(stdin, stdin):
    str1 = str1.rstrip()
    str2 = str2.rstrip()
    print(
        needleman_wunsnchs(str1,
                           str2, match=1, mismatch=0, gap=0))
