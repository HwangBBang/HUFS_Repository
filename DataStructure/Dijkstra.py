import math
"""
Graph - Part 2
Slide # 27
(Find shortest distances of all the vertices, from the source vertex 0)
(using Dijkstra's algorithm)
"""

# build the graph using adj. matrix M

class Graph:
    def __init__(self, num_of_vertices=7):
        self.N = num_of_vertices
        self.M = M = [[0 for _ in range(self.N)] for _ in range(self.N)]

    def insert_edge(self, v1, v2, weight):
        self.M[v1][v2] = weight
        self.M[v2][v1] = weight

    def adjacent_vertices(self, v):
        vertices = []
        for w in range(self.N):
            if self.M[v][w] > 0:
                vertices.append(w)
        return vertices


g = Graph(num_of_vertices=7)
g.insert_edge(0,4,3)
g.insert_edge(0,1,7)
g.insert_edge(0,5,10)
g.insert_edge(1,4,2)
g.insert_edge(1,5,6)
g.insert_edge(1,3,10)
g.insert_edge(1,2,4)
g.insert_edge(2,3,2)
g.insert_edge(3,5,9)
g.insert_edge(3,6,4)
g.insert_edge(3,4,11)
g.insert_edge(4,6,5)

source = 0

# initialize the cloud that includes known/visited vertices
S = []

# initialize the shortest distances to all the vertices
D = [math.inf for _ in range(g.N)]  # distance-to-all-vertices = infinity
D[source] = 0  # distance to source(self) is zero

while len(S) < g.N: # while there are unvisited vertices
    # I. find the vertex with min distance, among the unknown vertices
    print(len(S))
    v_min = None
    min_dist = math.inf
    for v in range(g.N):
        if v in S: # already visited/known in the cloud
            continue
        if D[v]<min_dist:
            min_dist = D[v]
            v_min = v
    print(v_min)
    # II. add <v_min> to the cloud
    S.append(v_min)

    # III. relax the all the adjacent edges from <v_min>
    for z in g.adjacent_vertices(v_min):
        if D[v_min]+g.M[v_min][z] < D[z]:
            D[z] = D[v_min]+g.M[v_min][z]

print(D)







