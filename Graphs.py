from queue import Queue
graph = {
    "A" : ["B", "C", "D"],
    "B" : ["A", "E"],
}

class GraphAL:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        print("add_vertex function")
        # Add vertex to the graph
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2):
        print("add_edge function")
        if v1 in self.graph and v2 in self.graph:
            if v1 != v2 and v2 not in self.graph[v1]:
                print("Adding an edge from v1 to v2.")
                self.graph[v1].append(v2)
                print("Adding an edge from v2 to v1.")
                self.graph[v2].append(v1)
        else:
            print("One or both vertices not found in the graph!")

    def display(self):
        print("display function")
        for v, edges in self.graph.items():
            print("Inside the for loop")
            print(f"{v}: {edges}")

class GraphMatrix:
    def __init__(self, num_v):
        print("Constructor")
        self.num_v = num_v
        self.vertices = []
        self.matrix = []
        self.graph = [[0] * num_v for _ in range(num_v)]
        self.queue = []

    def add_vertex(self, v):
        print("add_vertex function")
        if v not in self.vertices:
            self.vertices.append(v)
            # Expand each row in the matrix
            for row in self.matrix:
                row.append(0)
            # Add new row
            self.matrix.append([0] * len(self.vertices))

    def add_edge(self, v1, v2, w):
        print("add_edge function")
        # v1 and v2 are not the vertices themselves but the index they are associated with.
        if 0 <= v1 <= self.num_v and 0 <= v2 <= self.num_v:
            self.matrix[v1][v2] = w
            self.matrix[v2][v1] = w
        else:
            print(f"Error: Vertex out of bounds")

    def remove_edge(self, v1, v2):
        print("remove_edge function")
        if v1 in self.vertices and v2 in self.vertices:
            self.matrix[v1][v2] = 0
            self.matrix[v2][v1] = 0
        else:
            print(f"Error: Vertex out of bounds")

    def display(self):
        for row in self.matrix:
            print(row)

    def deque(self, v):
        return self.matrix.index(v)

    def bfs(self, start_v):
        # set up visited set and the queue
        visited = set()
        queue = [start_v]


        # While queue is not empty
        while queue:
            # Remove the front and print
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
            print(current)
            # Add all unvisited nodes to the printed node to the back
            # of the queue, set them as visited.
            for adj in self.graph[current]:
                if adj not in visited:
                    queue.append(adj)

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
            for adj in self.graph[current]:
                # For neighbor in adj list add to stack if not in visited.
                if adj not in visited:
                    stack.append(adj)

    def shortest_path(self, start_v, end_v):
        # Choose the job with the highest profit available at the moment.

        # Check if this job can be completed before its deadline.
        # If feasible, include the job in the final solution.
        # Repeat until no further jobs can be added without violating the deadline constraint.



def main():
    graph = GraphAL()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("A", "D")
    graph.add_edge("B", "A")
    graph.add_edge("B", "E")
    print(graph.display())

    print("\n=== Adjacency Matrix ===")
    graph_matrix = GraphMatrix()
    for v in ["A", "B", "C", "D", "E"]:
        graph_matrix.add_vertex(v)

    graph_matrix.add_edge("A", "B", 1)
    graph_matrix.add_edge("A", "C", 1)
    graph_matrix.add_edge("A", "D", 1)
    graph_matrix.add_edge("B", "E", 1)
    graph_matrix.add_edge("B", "C", 10)
    graph_matrix.display()

    # Remove an edge and display again
    graph_matrix.remove_edge("A", "B")
    graph_matrix.remove_edge("A", "D")
    print("After removing edge (A, B):")
    graph_matrix.bfs("A")
    graph_matrix.display()

if __name__ == "__main__":
    main()