# I get some tips with ChatGPT
platforms_base = [0] * 10_001

platforms_amount = int(input())
platforms = []

for _ in range(platforms_amount):
    altitude, start_point, end_point = map(int, input().split())
    platforms.append((altitude, start_point, end_point))

sorted_platforms = sorted(platforms, key=lambda x: x[0])
total_sum = 0
for plataform in sorted_platforms:
    # Considers that all the pillars were displaced 0.5 to the left
    total_sum += plataform[0] - platforms_base[plataform[1]]
    total_sum += plataform[0] - platforms_base[plataform[2] - 1]
    platforms_base = (
        platforms_base[: plataform[1]]
        + [plataform[0]] * (plataform[2] - plataform[1])
        + platforms_base[plataform[2] :]
    )

print(total_sum)
