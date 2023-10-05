def kmp_search(sentence, pattern):
    sentence_len = len(sentence)
    pattern_len = len(pattern)
    lps = get_lps(sentence, pattern)

    sentence_idx, pattern_idx = 0, 0
    while(sentence_idx<sentence_len):
        if(sentence[sentence_idx]==pattern[pattern_idx]):
            sentence_idx += 1
            pattern_idx += 1 
        if(pattern_idx == pattern_len):
            print(f"Found pattern at index {i-j}")
            pattern_idx = lps[pattern_idx-1]
        else:
            if sentence_idx<sentence_len and sentence[sentence_idx]=!pattern[pattern_idx]:
                