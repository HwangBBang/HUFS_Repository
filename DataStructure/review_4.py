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
        self.N = num_of_vertices        # vertex의 수 = 7개
        self.M = M = [[0 for _ in range(self.N)] for _ in range(self.N)]

    def insert_edge(self, v1, v2, weight):
        self.M[v1][v2] = weight # edge 의 길이
        self.M[v2][v1] = weight
    # v에 근접한 vertex 찾기
    def adjacent_vertices(self, v):
        vertices = []       #근접한 vertex를 담을 리스트         
        for other_vertex in range(self.N):      # 모든 vertex 탐색
            if self.M[v][other_vertex] > 0:     # Edge의 길이 > 0 이라면 / 근접했다면
                vertices.append(other_vertex)   # 리스트에 근접한 vertex 추가
        return vertices         # 근접한 vertex 가 담긴 리스트         

#vertex가 7 개인 그래프 g 생성
g = Graph(num_of_vertices=7)    
# edge 추가(vertex1, vertex2, 길이)
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

# 주어진 vertex의 이름: 0
source = 0  

#  클라우드 (방문한 vertices)초기화
cloud = []

# 모든 vertex의 최단거리 초기화
Distance = [math.inf for _ in range(g.N)]  # 시작 으로부터의 모든 거리를 무한대로 세팅
Distance[source] = 0    # 주어진 vertex와 주어진 vertex 거리는 0이므로 0으로세팅

# 방문하지 않는 vertex가 있는 동안 
while len(cloud) < g.N:  # cloud 의 갯수 = 방문한 vertex 의 갯수  /g.N : 그래프의 vertex 갯수
    # I.방문 하지 않은 vertex 가장 짧은 거리의 vertex찾기
    print(len(cloud))
    min_vertex = None           # 가장 가까운 vertex 초기화    
    min_distance = math.inf     # 가장 가까운 vertex의 거리 초기화
    
    for vertex in range(g.N):   # 모든 vertex를 탐색
        if vertex in cloud:     # 이미 방문한 vertex 라면
            continue            # 건너뛰어
        
        if Distance[vertex] < min_distance:     # vertex의 거리 < 현재 최소거리
            min_distance =  Distance[vertex]    # 현재 최소거리를 초기화
            min_vertex = vertex
    print(min_vertex)
    # II. min_vertex 을 cloud 에 추가
    cloud.append(min_vertex)
    
    # III. min_verte 의 인접한 Edge의 길이를 최소화 시킨다.
    for nearVertex in g.adjacent_vertices(min_vertex):  #min_vertex의 근접한 vertex 들 중에서
        # min_vertex의 길이 + 인접한 Edge의 길이 < near[nearVertex] 이라면 
        if Distance[min_vertex]+g.M[min_vertex][nearVertex] < Distance[nearVertex]:
            Distance[nearVertex] = Distance[min_vertex]+g.M[min_vertex][nearVertex] # 초기화한다.

print(Distance)