# import necessary libraries
import heapq

# define the function
def dijkstra(graph, start, end):

    # initialize the distances to infinity and the visited set to empty
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    # create a priority queue for the nodes
    queue = []
    heapq.heappush(queue, [0, start])

    # loop until the queue is empty
    while queue:

        # get the current node from the queue
        _, current_node = heapq.heappop(queue)

        # if the current node is the end node, return the distance
        if current_node == end:
            return distances[current_node]

        # if the current node has not been visited, update its neighbors
        if current_node not in visited:

            # update the distances of the neighbors and add them to the queue
            for neighbor, weight in graph[current_node].items():
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, [distance, neighbor])

            # add the current node to the visited set
            visited.add(current_node)

    # if the end node is not reached, return infinity
    return float('inf')

# create a graph with the list of current nodes, connected nodes, and path costs
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6},
}

# test the function
print(dijkstra(graph, 'A', 'E'))  # should return 4
