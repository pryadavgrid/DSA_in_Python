class Graph:

    def __init__(self, vertex):
        self.matrix = [ [0]*vertex for i in range(vertex) ]
        self.size = vertex


    def add_edge(self, src, dst, weight = None):
        if  self.size < src < 0 and dst > self.vertex < 0 :
            print("invalid edge")
            return
        
        # if undirected graph
        self.matrix[src][dst] = 1
        self.matrix[dst][src] = 1

        # if directed graph
        # self.matrix[src][dst] = 1

        # if weighted graph
        # self.matrix[src][dst] = weight

    def show_graph_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

        
graph = Graph(5)


# (0) ---- (2)
#  |        |   \
#  |        |     (4)
#  |        |   /
# (1) ---- (3)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(3,4)

graph.show_graph_matrix()