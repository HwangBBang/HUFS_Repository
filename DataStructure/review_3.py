class Graph:
    def __init__(self, num_of_vertices = 1000):
        self.N = num_of_vertices 
        self.M = [[0 for _ in range(N)] for _ in range(N)]
    
    def insert_edge(self, vertex1, vertex2):
        # vertex간의 Edge연결을 2차원 배열(행렬)로 표현
        self.M[vertex1][vertex2] = 1    # 0 일때 끊김
        self.M[vertex2][vertex1] = 1    # 1 일때 연결
    def adjacent_vertices(self, vertex):
        # vertex의 인접한 vertices 찾기
        verList = []        #인접한 vertex 담을 빈 리스트 생성
        for other_vertex in range(self.N):  #모든 vertex 순회
            if self.M[vertex][other_vertex] == 1:   #vertex와 연결된 다른 vertex가 있다면
                verList.append(other_vertex)        #verList에 other_vertex를 추가
        return verList      #other_vertex가 들어있는 verList를 반환

class DFS:
    def __init__(self, graph):
        # gragp의 정보
        self.graph = graph
        self.N = graph.N
        
        # Vertex 와 Edge 의 Labels
        self.UNEXPLORED, self.VISITED = 'unxp', 'vstd'      # UNEXPLORED에는 vertex , edge 두 가지가 있음
        self.DISCOVERY, self.BACK = 'dscv', 'back'
        
        # Vertex 와 Edge 의 Label 초기화
        self.vertex_label = [self.UNEXPLORED for _ in range(N)]
        self.edge_label = [[self.UNEXPLORED for _ in range(N)] for _ in range(N)]
        
        # DFS 의 Vertex 방문 순서
        self.visit_order = []
        
        # DFS 실행
        for vertex in range(self.N):    # 모든 vertex 확인
            if self.vertex_label[vertex] == self.UNEXPLORED:    # vertex의 레이블이 방문X 라면
                self.dfs(vertex)        # dfs 실행 (vertex가 출발점)
    
    def dfs(self, vertex):
        self.vertex_label[vertex] = self.VISITED  # 시작점이니까 레이블을 방문으로 초기화
        self.visit_order.append(vertex)      # 방문했으니까 방문 순서에 기입
        
        nearVertexList = self.graph.adjacent_vertices(vertex) # vertex의 근접 vertex 리스트 불러오기
        for nearVertex in nearVertexList:
            # Edge(vertex와 근처vertex 사이)의 레이블이 방문X 이라면
            if self.edge_label[vertex][nearVertex] == self.UNEXPLORED and self.edge_label[nearVertex][vertex] == self.UNEXPLORED:
                # 근처 vertex의 레이블이 UNEXPLORED 이라면
                if self.vertex_label[nearVertex] == self.UNEXPLORED:
                    # vertex에서 근처 vertex로가는 Edge 를 DISCOVERY로 초기화
                    self.edge_label[vertex][nearVertex] = self.DISCOVERY
                    # dfs 실행 (근처 vertex가 출발점)
                    self.dfs(nearVertex)
                # 근처 vertex의 레이블이 VISITED 이라면
                else:
                    # vertex에서 근처 vertex로가는 Edge 를 BACK 초기화
                    self.edge_label[vertex][nearVertex] = self.BACK

# Input: number of vertices
# and initialize Graph
N = int(input())
graph = Graph(N)
	
# Input: edge_list
edges = input() # format: 1,2 0,1 2,3
edges = edges.split() # : ['1,2', '0,1', '2,3']
	
# Mark edges in G
for e in edges:
	u,v = e.split(",")
	u,v = int(u), int(v)
	graph.insert_edge(u,v)

# Run DFS
runDFS = DFS(graph)
print('visit_order:', end=" ")
print(runDFS.visit_order)
print('E_label:')

print("    ", end=" ")
for j in range(graph.N):
	print('{:4d}'.format(j), end=" ")
print()

i =  0
for rows in runDFS.edge_label:
	print("{:4d}".format(i), end=" "); i += 1
	for x in rows:
		if x == runDFS.UNEXPLORED: print("....", end=" ")
		else: print(x, end=" ")
	print()

	
	
	
	
	