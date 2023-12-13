# I read the problem tip
n, k = map(int, input().split())
model = [input() for _ in range(n)]

picture = []

for x in range(n**k):
    aux_row = ''
    for y in range(n**k):
        point = '.'
        for z in range(k):
            orig_x = (x//(n**z)) % n
            orig_y = (y//(n**z)) % n
            if model[orig_x][orig_y] == '*':
                point = '*'
        aux_row += point
    picture.append(aux_row)

for row in picture:
    print(row)
