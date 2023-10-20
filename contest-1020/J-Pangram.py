string_len = int(input())
string = input().lower()
# If it have fewer letters than the alphabet the string is not a pangram
if(string_len < 26):
    print("NO")
else:
    string_set = set(string)

    # Generates all the letters of the alphabet
    alphabet = set()
    for letter in range(97, 123):
        alphabet.add(chr(letter))
    
    # Check the intersection between the string and alphabet sets   
    if(len(alphabet.intersection(string_set)) == 26):
        print("YES")
    else:
        print("NO")
