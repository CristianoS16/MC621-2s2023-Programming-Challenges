# Based on the solution shown in problem solving on the day 2023/10/20
# I used chatGPT to generate the functions to count the number of inversions
def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_count = count_inversions(arr[:mid])
    right_half, right_count = count_inversions(arr[mid:])

    merged, merge_count = merge_and_count_inversions(left_half, right_half)

    total_count = left_count + right_count + merge_count

    return merged, total_count


def merge_and_count_inversions(left, right):
    result = []
    count = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += len(left) - i

    result.extend(left[i:])
    result.extend(right[j:])

    return result, count


alphabet_dict = {
    "a": [0, []],
    "b": [0, []],
    "c": [0, []],
    "d": [0, []],
    "e": [0, []],
    "f": [0, []],
    "g": [0, []],
    "h": [0, []],
    "i": [0, []],
    "j": [0, []],
    "k": [0, []],
    "l": [0, []],
    "m": [0, []],
    "n": [0, []],
    "o": [0, []],
    "p": [0, []],
    "q": [0, []],
    "r": [0, []],
    "s": [0, []],
    "t": [0, []],
    "u": [0, []],
    "v": [0, []],
    "w": [0, []],
    "x": [0, []],
    "y": [0, []],
    "z": [0, []],
}

string_len = int(input())
string = input()
inverted_string = string[::-1]

# Add the position in which each letter is found in the dictionary of letters
for i in range(string_len):
    alphabet_dict[string[i]][1].append(i)

# The minimum displacement map always put the left to the smallest position of the current letter
displacement_map = []
for letter in inverted_string:
    displacement_map.append(alphabet_dict[letter][1][alphabet_dict[letter][0]])
    alphabet_dict[letter][0] += 1

# Uses an adaptation of Merge Sort to find the number of inversions, as shown in Samuel's solution
sorted_arr, inversions = count_inversions(displacement_map)
print(inversions)
