n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]

# Build the graph using adjacency list
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# Defines auxiliary lists
current_squawks = [0] * n
new_squawks = [0] * n
current_squawks[s] = 1

# Simula a passagem do tempo t
for _ in range(t):
    # Performs the spread of squawks for the neighbors of the infected nodes
    for i in range(n):
        if current_squawks[i] > 0:
            for j in graph[i]:
                new_squawks[j] += current_squawks[i]
    current_squawks = new_squawks.copy()
    new_squawks = [0] * n

print(sum(current_squawks))
