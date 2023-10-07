from sys import stdin

# Implementation of the LPS algorithm as shown in class
def compute_lps_array(sentence, pattern):
    lps = [0] * len(pattern)
    lps_len = 0

    i = 1
    while(i < len(pattern)):
        if(pattern[i] == pattern[lps_len]):
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
    lps = compute_lps_array(sentence, pattern)

    sentence_idx, pattern_idx = 0, 0
    while(sentence_idx < sentence_len):
        if(sentence[sentence_idx] == pattern[pattern_idx]):
            sentence_idx += 1
            pattern_idx += 1
        if(pattern_idx == pattern_len):
            # Returns True when you first find the pattern
            return True
            pattern_idx = lps[pattern_idx-1]
        else:
            if sentence_idx < sentence_len and sentence[sentence_idx] != pattern[pattern_idx]:
                if (pattern_idx != 0):
                    pattern_idx = lps[pattern_idx-1]
                else:
                    sentence_idx += 1
    # Returns fake if you don't find the pattern
    return False


for line in stdin:
    # Makes String in Lowercase to facilitate the search
    print("yes" if kmp_search(line.upper(), 'PROBLEM') else "no")
