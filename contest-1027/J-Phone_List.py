tests_number = int(input())
while(tests_number):
    tests_number -= 1

    number_of_phones = int(input())
    prefix_set = set()
    phones_set = set()
    is_consistent = True

    for _ in range(number_of_phones):
        currente_phone = input()
        if currente_phone in phones_set:
            is_consistent = False
        phones_set.add(currente_phone)
        for i in range(1, len(currente_phone)):
            prefix_set.add(currente_phone[:-i])

    if(phones_set & prefix_set):
        is_consistent = False

    print("YES" if is_consistent else "NO")
