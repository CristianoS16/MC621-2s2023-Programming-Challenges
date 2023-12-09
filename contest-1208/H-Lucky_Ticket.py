n = int(input())
number = input()

is_lucky = False
match_sum = False
if number.replace("4", "").replace("7", "") == "":
    is_lucky = True

if sum([int(digit) for digit in number[0 : n // 2]]) == sum(
    [int(digit) for digit in number[n // 2 :]]
):
    match_sum = True

print("YES" if is_lucky and match_sum else "NO")
