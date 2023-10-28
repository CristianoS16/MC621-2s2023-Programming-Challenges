# Based on the solution shown in problem solving on the day 2023/10/20

# Implementation of the LPS algorithm as shown in class
def compute_lps_array(sentence, pattern):
    pattern_len = len(pattern)
    lps = [0] * pattern_len
    lps_len = 0

    i = 1
    while(i < pattern_len):
        if(sentence[i] == sentence[lps_len]):
            lps_len += 1
            lps[i] = lps_len
            i += 1
        else:
            if(lps_len != 0):
                lps_len = lps[lps_len-1]
            else:
                lps[i] = 0
                i += 1
    return lps

# Implementation of Algotmo KMP as seen in class
def kmp_search(sentence, pattern):
    sentence_len = len(sentence)
    pattern_len = len(pattern)
    if pattern_len > sentence_len:
        return 0
    lps = compute_lps_array(sentence, pattern)
    found_patterns_count = 0

    sentence_idx, pattern_idx = 0, 0
    while(sentence_idx < sentence_len):
        if(sentence[sentence_idx] == pattern[pattern_idx]):
            sentence_idx += 1
            pattern_idx += 1
        if(pattern_idx == pattern_len):
            found_patterns_count += 1
            pattern_idx = lps[pattern_idx-1]
        else:
            if sentence_idx < sentence_len and sentence[sentence_idx] != pattern[pattern_idx]:
                if (pattern_idx != 0):
                    pattern_idx = lps[pattern_idx-1]
                else:
                    sentence_idx += 1
    return found_patterns_count


while True:
    string = input()

    if string == '.':
        break

    if string == '':
        print(0)
        continue

    # Uses kmp to compute the number of occurrences of the pattern
    print(kmp_search(string+string, string)-1)
