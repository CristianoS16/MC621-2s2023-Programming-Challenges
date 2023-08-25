tests_number = int(input())

while(tests_number):
    n, k = map(int, input().split())
    array = [int(n) for n in input().split()]
    count = 0
    current_seq = 0

    for i in range(n-1):
        # if ai >= 2*ai+1, so is not possible that ai*2^K < ai+1*2^k+1 because
        # ai*2^K < ai+1*2*2^k that is the same of ai < ai+1*2
        # So the current sequence is blocken, start again from zero
        if(array[i] >= 2 * array[i+1]):
            current_seq = 0
        else:
            current_seq += 1

        # If the current sequence has more than k elements there are a new subarray inside it
        if current_seq >= k:
            count += 1

    print(count)

    tests_number -= 1
