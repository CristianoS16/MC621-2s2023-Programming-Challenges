tests_number = int(input())

while(tests_number):
    tests_number -= 1

    input_list = input().split()
    number_players = int(input_list[0])
    prob = float(input_list[1])
    winner_idx = int(input_list[2])

    # Calculates the base of probability
    final = prob * (1 - prob) ** (winner_idx-1)

    acc = final
    prev_acc = 0
    round_factor = (1-prob) ** number_players

    # Calculates the probability of the desired result occurs in a new round is accumulated with the previous probabilities
    # Stop interacting when the difference between results presents the desired accuracy
    while (round(prev_acc, 6) != round(acc, 6)):
        prev_acc = acc
        final *= round_factor
        acc += final

    print("{:.4f}".format(acc))
