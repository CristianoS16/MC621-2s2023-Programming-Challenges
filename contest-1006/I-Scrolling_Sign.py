tests_number = int(input())
while(tests_number):
    tests_number -= 1

    characters_sing, words_number = map(int, input().split())
    final_string = input()
    for _ in range(words_number-1):
        current_word = input()

        # Travels both sings looking for the match point
        for i in range(characters_sing, -1, -1):
            if final_string[-i:] == current_word[:i] or i == 0:
                # Concatena the strings to optimize characters
                final_string += current_word[i:]
                break

    print(len(final_string))
