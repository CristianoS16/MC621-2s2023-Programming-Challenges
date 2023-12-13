dictionary = []
plates = []
dict_len, plates_len = map(int, input().split())
for _ in range(dict_len):
    dictionary.append(input())

for _ in range(plates_len):
    found_word = "No valid word"
    letter1, letter2, letter3 = input().lower()

    # Words go to check the order of the letters
    for word in dictionary:

        # Search for the index of the first occurrence of the first letter sought
        start_idx = word.find(letter1)
        if start_idx == -1:
            continue
        # Search for the index of the last occurrence of the last letter sought
        end_idx = word[::-1].find(letter3)
        if end_idx == -1:
            continue
        # Check if there is the second letter sought between the indexes defined previously
        if word[start_idx+1:-end_idx-1].find(letter2) != -1:
            found_word = word
            break

    print(found_word)
