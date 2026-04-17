from collections import deque 
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for nieghbour in graph[node]:
            if nieghbour not in visited:
                visited.add(nieghbour)
                queue.append(nieghbour)
graph = {
        'A' : ['B','C'],
        'B' : ['D'],
        'C' : ['D'],
        'D' : []
    }
bfs(graph,'A')

