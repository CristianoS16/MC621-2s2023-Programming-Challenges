import math

n = int(input())
phone_number = input()

# Determines the amount of movements
number_of_moves = n - 11
vasya_moves = math.ceil(number_of_moves/2)
petya_moves = math.floor(number_of_moves/2)

phone_gaps = phone_number.split("8")

# Determines how much 8's it is possible to group at the beginning of the string
total_8_group = 0
for i in range(len(phone_gaps)):
    vasya_moves -= len(phone_gaps[i])
    if vasya_moves < 0:
        break
    total_8_group += 1

# Checks if is possible that Petya erase all 8's in the beggining of the string
print("YES" if total_8_group > petya_moves else "NO")
