from math import comb

MOD_BASE = 10**9 + 7

tests_number = int(input())
while(tests_number):
    tests_number -= 1

    bloggers_qty, contract_qty = map(int, input().split())
    followers = [int(n) for n in input().split()]

    # Order the list of followers to get the largest through a slice
    followers.sort()
    contracted_bloggers = followers[-contract_qty:]

    # Checks the amount of bloggers embarrassed with the smallest number of
    # followers that are still among those with the highest number of followers
    selected_bloggers_with_smallest_followers = contracted_bloggers.count(
        contracted_bloggers[0])
    # Check the total number of bloggers with the number of followers that correspond to the least to be selected
    total_bloggers_with_smallest_followers = followers.count(
        contracted_bloggers[0])
    # Makes the combination to find how many ways possible and it is possible to select the
    # number of bloggers that will be included to get the highest sum of the total bloggers with that amount of followers
    final_result = comb(total_bloggers_with_smallest_followers,
                        selected_bloggers_with_smallest_followers)
    print(final_result % MOD_BASE)
