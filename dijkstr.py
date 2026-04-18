import heapq
def dijkstra(graph, source):
    #Intialize distances
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    
    # min heap (distance, node)
    pq = [(0, source)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        # skip if already found better path
        if current_dist > dist[current_node]:
            continue
        # explore neigbhours
        for neigbhor, weight in graph[current_node]:
            distance = current_dist + weight
        
        # Relaxation
        if distance < dist[neigbhor]:
            dist[neigbhor] = distance
            heapq.heappush(pq, (distance, neigbhor))

    return dist

# example graph (Adjacency List)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

result = dijkstra(graph, 'A')
print(result)