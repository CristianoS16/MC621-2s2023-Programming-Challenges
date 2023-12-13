digits_list = [0]
for i in range(1, 500):
    digits_list.append((digits_list[-1] + int(str(i**i)[-1])) % 10)
print(digits_list)
print(len(digits_list))

# n = int(input())

# while n != 0:
#     # Run the given formula by adding the digits to a list that is reused for the next input
#     digits_list_len = len(digits_list)
#     if digits_list_len < n+1:
#         for i in range(digits_list_len, n+1):
#             digits_list.append((digits_list[-1] + int(str(i**i)[-1])) % 10)
#     print(digits_list)
#     print(digits_list[n])

#     result = n*(n+1)//2
#     print(result)

#     n = int(input())
