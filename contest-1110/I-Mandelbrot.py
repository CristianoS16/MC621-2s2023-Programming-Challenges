from sys import stdin

count = 0
for line in stdin:
    count += 1
    line = line.split()
    x = float(line[0])
    y = float(line[1])
    sequence_len = int(line[2])

    # https://pt.wikipedia.org/wiki/Conjunto_de_Mandelbrot
    output = "IN"
    new_x = new_y = 0
    for _ in range(sequence_len):
        aux_x = new_x
        new_x = new_x**2 - new_y**2 + x
        new_y = 2 * aux_x * new_y + y

        if new_x**2 + new_y**2 > 4:
            output = "OUT"
            break

    print(f"Case {count}: {output}")
