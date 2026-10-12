"""
Route Finding & Shortest Route

Implement the logic to find the shortest path from a source to a destination.
You can use Dijkstra's Algorithm or Breadth-First Search (BFS) for this.

Example input:
    routes = ROUTES (from routes.py)
    source = "Main Gate"
    destination = "Library"

Example output:
    (["Main Gate", "CSE Block", "Library"], 200)  # (route_list, total_distance)
"""


import heapq


def find_shortest_route(routes, source, destination):
    """
    Find the shortest route from source to destination.

    Return:
        tuple: (route_list, total_distance)
        If no route exists, return ([], 0).
    """
    if not routes or source not in routes or destination not in routes:
        return ([], 0)

    if source == destination:
        return ([source], 0)

    distances = {node: float("inf") for node in routes}
    distances[source] = 0
    previous_nodes = {node: None for node in routes}

    # Priority queue stores tuples of (distance, current_node)
    pq = [(0, source)]
    visited = set()

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == destination:
            break

        for neighbor, weight in routes.get(current_node, {}).items():
            if neighbor not in routes:
                continue
            distance = current_dist + weight
            if distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    if distances.get(destination, float("inf")) == float("inf"):
        return ([], 0)

    # Reconstruct the shortest path from source to destination
    path = []
    curr = destination
    while curr is not None:
        path.append(curr)
        curr = previous_nodes[curr]
    path.reverse()

    return (path, distances[destination])


