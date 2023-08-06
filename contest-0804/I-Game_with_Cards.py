tests_number = int(input())

while(tests_number):
    n = int(input())
    alice_cards = [int(n) for n in input().split()]
    n = int(input())
    bob_cards = [int(n) for n in input().split()]

    # Get the greatest number of each player
    alice_max = max(alice_cards)
    bob_max = max(bob_cards)

    # Make comparations to define the winner
    if(alice_max > bob_max):
        print("Alice")
        print("Alice")
    elif (bob_max > alice_max):
        print("Bob")
        print("Bob")
    else:
        print("Alice")
        print("Bob")

    tests_number -= 1
