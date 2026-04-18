from collections import deque
graph = {
    'A':[('B',5), ('C',2)],
    'B':[('D',3)],
    'C':[('D',4)],
    'D':[]
}
print("Weighted Graph:")
for node in graph:
    print(node, "->", graph[node])

def bfs_weighted(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end = " ")
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
print("\nBFS on Weighted Graph:")
bfs_weighted(graph,'A')