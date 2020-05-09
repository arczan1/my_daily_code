class Edge:
    """Represents edges of graph

    Atributes
    ---------
    start : str
        beginning of edge
    end : str
        ending of edge
    cost : float
        distence between start and end
    """
    def __init__(self, start: str, end: str, cost: float):
        self.start = start
        self.end = end
        self.cost = cost


class Graph:
    """This class is used to represent Graphs

    Attributes
    ----------
    vertices : set
        graph vertices
    edges : list
        graph edges
    is_directed:
        if True graph is directed if False graph is undirected
        In directed graph Edge("A", "B", 2) is diffrent from Edge("B", "A", 2)

    Methods
    -------
    get_neighbors(vertex: int)
        Returns vertex neighbors(with cost)
    shortest_path(source: str, target: str)
        Returns shortest path from source to target using Dijkstra's algorithm
    """
    def __init__(self, vertices: set, edges: list, is_directed=False):
        """
        Parameters
        ----------
        vertices : set
            Set of vertices, example: set(["A", "B", "C"])
        edges : list
            List of edges, example: [Edge("A", "B", 3), Edge("B", "C", 2)]
        is_directed : bool, optional
            specify if graph is directed or undirected(default is False)
        """
        self.vertices = vertices
        self.edges = edges
        self.is_directed = is_directed

    def get_neighbors(self, vertex: int) -> list:
        """Returns list of neightbors(with distance) to the vertex

        Parameters
        ----------
        vertex : int
            vertex to check

        Returns
        -------
        list
            neighbors of vertex and distance between them
            Example:
                edges: [Edge("A", "B", 1), Edge("A", "C", 4)]
                get_neighbor("A") -> [("B", 1), ("C", 4)]
        """
        neighbors = []

        for edge in self.edges:
            if edge.start == vertex:
                # Neighbor found
                neighbors.append((edge.end, edge.cost))
            # if Graph is undirected check edge.end
            elif (not self.is_directed) and edge.end == vertex:
                # Neighbor found
                neighbors.append((edge.start, edge.cost))

        return neighbors

    def shortest_path(self, source: str, target: str) -> list:
        """
        Returns shortest path from source to target using Dijkstra's algorithm

        Parameters
        ----------
        source : str
            vertex that begins the path
        target : str
            vertex that ends the path

        Returns
        -------
        list
            path from source to target, example: ["A", "C", "B", "D"]
        """
        unvisited_vertices = set()
        # Distance from source to vertex
        distance = dict()
        # Previous vertex in path
        prev = dict()

        # Default values
        for i in self.vertices:
            unvisited_vertices.add(i)
            # Default distance for all vertices is infinity
            distance[i] = float("inf")
            # At the beginning all vertices don't have previous vertex
            prev[i] = None
        # distance from source to source is 0
        distance[source] = 0

        while unvisited_vertices:
            # Select vertex with the shortest distance
            ver = min(unvisited_vertices, key=distance.get)
            # Mark selected vertex as visited
            unvisited_vertices.remove(ver)

            for neighbor in self.get_neighbors(ver):
                # Calculate  distance between neighbor and current vertex
                new_distance = distance[ver] + neighbor[1]

                # Check if new path to neighbor is shorter than previous one
                if new_distance < distance[neighbor[0]]:
                    # Update distance of neighbor
                    distance[neighbor[0]] = new_distance
                    # Update neighbor previous vertex
                    prev[neighbor[0]] = ver

        # Build path from distance dictionary
        path = [target]
        tmp_vertex = target
        # End building path when previous element is None
        while prev[tmp_vertex] is not None:
            # Add vertex at the beginning of the path(building in
            # reversed order: from target to source)
            path.insert(0, prev[tmp_vertex])
            # change tmp_vertex to it's previous vertex
            tmp_vertex = prev[tmp_vertex]

        return path


if __name__ == "__main__":
    vertices = set([char for char in "ABCDEF"])
    print("""
       3      8
    A------B------C
    |     /|      |
   3|   2/ |7     |20
    |   /  |      |
    F--E---D------/
     3   3
    """)
    edges = [
            Edge("A", "F", 3),
            Edge("A", "B", 3),
            Edge("B", "E", 2),
            Edge("B", "D", 7),
            Edge("B", "C", 8),
            Edge("C", "D", 20),
            Edge("D", "E", 3),
            Edge("E", "F", 3),
            ]
    g = Graph(vertices, edges)

    print("Shortest path from C to D: ")
    for i in g.shortest_path("C", "D"):
        print(i, end=" ")
    print("\nShortest path from A to D: ")
    for i in g.shortest_path("A", "D"):
        print(i, end=" ")
    print("")
