def check_symmetry(sorted_list, threshold):
    list_len = len(sorted_list)
    if list_len % 2 == 1:
        middle = sorted_list.pop(list_len // 2)
        if middle != threshold:
            return False
    for i in range(len(sorted_list) // 2):
        if (sorted_list[i] + sorted_list[-i - 1]) / 2 != threshold:
            return False
    return True


tests_number = int(input())
while tests_number:
    tests_number -= 1

    points_len = int(input())
    points = dict()

    for _ in range(points_len):
        x, y = map(int, input().split())
        if y in points.keys():
            points[y].append(x)
        else:
            points[y] = [x]

    threshold = (
        points[y][0] if len(points[y]) == 1 else (min(points[y]) + max(points[y])) / 2
    )

    output = "YES"
    for y in points.keys():
        if not check_symmetry(sorted(points[y]), threshold):
            output = "NO"
            break

    print(output)
