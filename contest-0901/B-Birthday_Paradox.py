# I use wikipedia Birthday Problem as base: https://en.wikipedia.org/wiki/Birthday_problem

tests_number = int(input())

for i in range(tests_number):

    days = int(input())
    count = 0
    prob_inv = 1

    while prob_inv > 0.5:
        count += 1
        prob_inv *= (1-count/days)

    print(f"Case {i+1}: {count}")
