# Travels parts of the sentence with the same size as the pattern sought and compares with it
def find_pattern_indices(sentence, pattern):
    sentence_len = len(sentence)
    pattern_len = len(pattern)
    if pattern_len > sentence_len or pattern not in sentence:
        return []
    found_patterns = []
    for i in range(sentence_len-pattern_len+1):
        if sentence[i:i+pattern_len] == pattern:
            found_patterns.append(i+1)

    return found_patterns


tests_number = int(input())
while(tests_number):
    tests_number -= 1

    sentence, pattern = input().split(" ")

    idx_list = find_pattern_indices(sentence, pattern)

    if(len(idx_list) == 0):
        print("Not Found")
    else:
        print(len(idx_list))
        print(*idx_list)
    if(tests_number != 0):
        print()
