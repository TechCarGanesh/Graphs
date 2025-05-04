import random
import heapq
from queue import Queue
NUM_LANDMARKS = 14

graph = {
    "Central Park": ["Fifth Avenue", "Metropolitan Museum of Art", "Wall Street"],
    "Fifth Avenue": ["Central Park", "Empire State Building"],
    "Times Square": ["Broadway", "Empire State Building", "Grand Central Terminal"],
    "Broadway": ["Times Square", "Rockefeller Center"],
    "Empire State Building": ["Chrysler Building", "Fifth Avenue", "Times Square"],
    "Wall Street": ["One World Trade Center"],
    "Grand Central Terminal": ["Chrysler Building", "Rockefeller Center", "One World Trade Center", "Times Square"],
    "Rockefeller Center": ["One World Trade Center", "Grand Central Terminal", "Broadway"],
    "Metropolitan Museum of Art": ["Central Park", "One World Trade Center"],
    "Chrysler Building": ["Grand Central Terminal", "Wall Street", "Empire State Building"],
    "One World Trade Center": ["Wall Street", "Rockefeller Center", "Grand Central Terminal",
                               "Metropolitan Museum of Art"]
}


class GraphAdjMatrix:
    def __init__(self, num_v):
        print("Constructor")
        self.num_v = num_v
        self.vertices = []
        self.vertex_indices = {}
        self.matrix = [[0] * num_v for _ in range(num_v)]
        # self.graph = [[0] * num_v for _ in range(num_v)]
        self.graph = [[]]
        self.queue = []

    def add_vertex(self, v):
        print("add_vertex function")
        if v not in self.vertex_indices:
            if len(self.vertices) < self.num_v:
                # Add vertex name
                self.vertex_indices[v] = len(self.vertices)
                self.vertices.append(v)

                # Expand existing rows in the matrix
                for row in self.graph:
                    row.append(v)

                # Add new row for the new vertex
                self.graph.append([0] * (len(self.vertices)))
            else:
                print("Maximum number of vertices reached.")
        else:
            print(f"Vertex '{v}' already exists.")

    def add_edge(self, v1, v2, w):
        print("add_edge function v1 ", v1, "v2 ", v2, "w ", w)
        # v1 and v2 are not the vertices themselves but the index they are associated with.
        # print("Graph vertices:", self.graph)
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertex_indices[v1]
            j = self.vertex_indices[v2]
            if v1 != v2 and v2 not in self.graph[i]:
                print("Adding an edge from v1 to v2.")
                self.graph[i][j] = v1
                self.graph[j][i] = v2
                self.matrix[i][j] = w
                self.matrix[j][i] = w  # For undirected graph
        else:
            print("One or both vertices not found in the graph!")

    def remove_edge(self, v1, v2):
        print("remove_edge function")
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertex_indices[v1]
            j = self.vertex_indices[v2]
            self.matrix[i][j] = 0
            self.matrix[j][i] = 0
        else:
            print(f"Error: Vertex out of bounds")

    def display(self):
        print("In display function")
        for v1 in self.vertices:
            i = self.vertex_indices[v1]
            for row in self.matrix[i]:
                print(row, end=' ')
            print()

    def deque(self, v):
        print("In deque function")
        return self.graph.index(v)

    def bfs(self, start_vertex):
        if start_vertex not in self.vertex_indices:
            print(f"Start vertex '{start_vertex}' not found in the graph.")
            return

        visited = set()
        queue = []

        visited.add(start_vertex)
        queue.append(start_vertex)

        print("\nBFS Traversal:")

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=" ")

            current_index = self.vertex_indices[current_vertex]
            for neighbor_index in range(len(self.vertices)):
                weight = self.graph[current_index][neighbor_index]
                if weight != 0:
                    neighbor_vertex = self.vertices[neighbor_index]
                    if neighbor_vertex not in visited:
                        visited.add(neighbor_vertex)
                        queue.append(neighbor_vertex)
        print()

    def dfs(self, start_v):
        # Set up visited and the stack with start vertex in the stack
        visited = set()
        stack = [start_v]

        # While our stack is not empty
        while stack is not None:
            # Remove from stack, if not in visited then print and add to visited
            current = stack.pop()
            if current not in visited:
                visited.add(current)
            print(current)
            # Add all unvisited nodes to the printed node to the back
            # of the stack, set them as visited.
            for lm in self.graph[current]:
                # For neighbor in adj list add to stack if not in visited.
                if lm not in visited:
                    stack.append()


    def shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.vertex_indices or end_vertex not in self.vertex_indices:
            print("One or both vertices not found in the graph.")
            return

        start_index = self.vertex_indices[start_vertex]
        end_index = self.vertex_indices[end_vertex]

        distances = {v: float('inf') for v in self.vertices}
        previous = {v: None for v in self.vertices}
        distances[start_vertex] = 0

        pq = [(0, start_vertex)]  # (distance, vertex)

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_vertex == end_vertex:
                break

            current_index = self.vertex_indices[current_vertex]

            for neighbor_index in range(len(self.vertices)):
                weight = self.matrix[current_index][neighbor_index]
                if weight != 0:
                    neighbor_vertex = self.vertices[neighbor_index]
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor_vertex]:
                        distances[neighbor_vertex] = new_distance
                        previous[neighbor_vertex] = current_vertex
                        heapq.heappush(pq, (new_distance, neighbor_vertex))

        # Reconstruct the path
        path = []
        current = end_vertex
        while current:
            path.append(current)
            current = previous[current]
        path.reverse()

        if distances[end_vertex] == float('inf'):
            print(f"No path found from '{start_vertex}' to '{end_vertex}'.")
        else:
            print(f"\nShortest path from '{start_vertex}' to '{end_vertex}': {' -> '.join(path)}")
            print(f"Total cost: {distances[end_vertex]}")


def main():
    city_net = GraphAdjMatrix(NUM_LANDMARKS)
    for landmark, edges in graph.items():
        print("Landmark ", landmark, "Edges ", edges)
        city_net.add_vertex(landmark)

    for landmark, edges in graph.items():
        for edge in edges:
            weight = random.randint(1,25)
            city_net.add_edge(landmark, edge, weight)

    city_net.bfs("Central Park")
    city_net.display()
    while True:
        print("Calculate the shortest path from ")
        print("Central Park")
        print("Fifth Avenue")
        print("Times Square")
        print("Broadway")
        print("Empire State Building")
        print("Wall Street")
        print("Grand Central Terminal")
        print("Rockefeller Center")
        print("Metropolitan Museum of Art")
        print("Chrysler Building")
        print("One World Trade Center")
        choice_1 = input(str("Enter Choice 1:"))
        choice_2 = input(str("Enter Choice 2:"))
        city_net.shortest_path(choice_1, choice_2)

if __name__ == "__main__":
    main()
