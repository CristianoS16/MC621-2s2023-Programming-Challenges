original_commands = input()
receved_commands = input()

# Count the number of commands sent
original_plus = original_commands.count("+")
original_minus = original_commands.count("-")
original_final_position = original_plus - original_minus

# Count the number of commands received
receved_plus = receved_commands.count("+")
receved_minus = receved_commands.count("-")
lost_commands = receved_commands.count("?")

total_prob = 2**lost_commands

# Computes the possible final positions
final_positions = [(receved_plus - receved_minus)]
for _ in range(lost_commands):
    aux = []
    for i in final_positions:
        aux += [i+1, i-1]
    final_positions = aux

print(final_positions.count(original_final_position)/total_prob)
