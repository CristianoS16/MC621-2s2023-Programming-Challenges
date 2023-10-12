def compute_lps_array(sentence, pattern):
    lps = [0] * len(pattern)
    lps_len = 0

    i = 1
    while(i < len(pattern)):
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


def kmp_search(sentence, pattern):
    sentence_len = len(sentence)
    pattern_len = len(pattern)
    if pattern_len > sentence_len:
        return []
    lps = compute_lps_array(sentence, pattern)
    found_patterns = []
    print("lps: ", lps)

    sentence_idx, pattern_idx = 0, 0
    while(sentence_idx < sentence_len):
        if(sentence[sentence_idx] == pattern[pattern_idx]):
            sentence_idx += 1
            pattern_idx += 1
        if(pattern_idx == pattern_len):
            print(f"Found pattern at index {sentence_idx-pattern_idx}")
            found_patterns.append(sentence_idx-pattern_idx)
            pattern_idx = lps[pattern_idx-1]
        else:
            if sentence_idx < sentence_len and sentence[sentence_idx] != pattern[pattern_idx]:
                if (pattern_idx != 0):
                    pattern_idx = lps[pattern_idx-1]
                else:
                    sentence_idx += 1
    return found_patterns


sentence_test = "AAAAABAAABA"
pattern_test = "AAA"
print(kmp_search(sentence_test, pattern_test))
