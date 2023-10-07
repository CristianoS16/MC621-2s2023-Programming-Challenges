tests_number = int(input())

# Check if the sound perceived is from a cat
def is_a_cat(pattern, sentence):
    pattern_idx = 0
    pattern_len = len(pattern)
    # See if the first character is correct
    if sentence[0] != 'm':
        return False
    # Runs through the string given by verifying the occurrence of the pattern
    for i in sentence:
        if pattern[pattern_idx] != i:
            if pattern_idx+1 < pattern_len and pattern[pattern_idx+1] == i:
                pattern_idx += 1
            else:
                return False
    # Check if the last character of the string is the same as the last of the pattern given
    return i == pattern[-1]


while(tests_number):
    tests_number -= 1

    sound_len = int(input())
    sound = input()

    print("YES" if is_a_cat("meow", sound.lower()) else "NO")
