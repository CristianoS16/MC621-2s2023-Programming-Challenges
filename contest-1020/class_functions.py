def print_table(table, m, n):
    for i in range(n):
        for j in range(m):
            print(table[i][j], end=' ')
        print()

# Get string alignment


def get_alignment(table, p, q, match=2, mismatch=-1, gap=-1):
    n = len(p) + 1
    m = len(q) + 1
    i, j = n - 1, m - 1

    alignment_p = []
    alignment_q = []

    # Travel over the table to recover alignment
    while i > 0 and j > 0:
        current_score = table[i][j]
        diagonal_score = table[i - 1][j - 1]
        left_score = table[i][j - 1]
        up_score = table[i - 1][j]

        if current_score == diagonal_score + (match if p[i - 1] == q[j - 1] else mismatch):
            alignment_p.append(p[i - 1])
            alignment_q.append(q[j - 1])
            i -= 1
            j -= 1
        elif current_score == up_score + gap:
            alignment_p.append(p[i - 1])
            alignment_q.append('-')
            i -= 1
        else:
            alignment_p.append('-')
            alignment_q.append(q[j - 1])
            j -= 1

    # Fill in with gaps in P
    while i > 0:
        alignment_p.append(p[i - 1])
        alignment_q.append('-')
        i -= 1

    # Fill in with remaining gaps in q
    while j > 0:
        alignment_p.append('-')
        alignment_q.append(q[j - 1])
        j -= 1

    # Invert the aligned sequences
    alignment_p = alignment_p[::-1]
    alignment_q = alignment_q[::-1]

    return ''.join(alignment_p), ''.join(alignment_q)

# Needleman Wunsnch’s algorithm as showed in the class


def needleman_wunsnchs(seq1, seq2, match=2, mismatch=-1, gap=-1):
    n = len(seq1)+1
    m = len(seq2)+1

    # Build table
    table = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        table[i][0] = i * gap
    for j in range(1, m):
        table[0][j] = j * gap

    for i in range(1, n):
        for j in range(1, m):
            # check for match, mismatch or gap
            value = match if seq1[i-1] == seq2[j-1] else mismatch
            table[i][j] = max(
                table[i-1][j-1] + value,
                table[i-1][j] + gap,
                table[i][j-1] + gap)

    print_table(table, m, n)
    print("score: ", table[n-1][m-1])
    str1, str2 = get_alignment(table, seq1, seq2, match, mismatch, gap)
    print(str1)
    print(str2)
    return str1, str2, table[n-1][m-1]


# needleman_wunsnchs('ACAATCC', 'AGCATGC')
# print(needleman_wunsnchs('TCTTCTTAATGCAGTCCTTTTAT', 'TCTTATTCAGTCATCTCTT'))

# needleman_wunsnchs('ADAM', "MADA", match=1, mismatch=0, gap=0)
# needleman_wunsnchs('MADAM', "MADAM", match=1, mismatch=0, gap=0)
# STR123 = "RACEF1CARFAST"
# needleman_wunsnchs(STR123, STR123[::-1], match=1, mismatch=0, gap=0)

# needleman_wunsnchs('DFLNQ1BANANAQWJIOPEJMOF', "KFNQWIEJHGBQBANAFOIQNW",
#                    match=1, mismatch=0, gap=0)

needleman_wunsnchs(
    "sorry",
    "scared", match=0, mismatch=1, gap=1)
