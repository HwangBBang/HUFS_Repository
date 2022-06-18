# BST   (이진 탐색 트리)
# 왼쪽key < 가운데key < 오른쪽key
class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.item = (key, value)
        self.left, self.right = left, right

    def key(self):
        return self.item[0]

    def value(self):
        return self.item[1]

    def set_value(self, value):
        self.item[1] = value

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
    # 재귀보다 Loop 를 활용한 것이 보다 효율적이다.
    def search(self, key):          #loop Ver / key값을 가진 노드를 찾는다.
        root = self.root
        while root is not None:     # root 노드가 존재하는동안 
            if key == root.key():   # 찾는 키 = 조사중인 키
                break               # while 문 탈출 / 조사중인 key값이 찾는값으로 초기화되어있음
            
            elif key < root.key():  # 찾는 키 < 조사중인 키 
                root = root.left    # 조사중인 키를 왼쪽으로 이동
            
            elif key > root.key():  # 찾는 키 > 조사중인 키
                root = root.right   # 조사중인 키를 오른쪽으로 이동
        #while 문 탈출
        return root                 # root의 key값이 찾는값으로 초기화된 상태
    # 재귀보다 Loop 를 활용한 것이 보다 효율적이다.
    def search_p(self, key):        # loop Ver / key 값을 가진 노드 + 그 노드의 부모도 찾는다.
        root = self.root
        parent = None
        while root is not None:     #root 노드가 존재하는동안
            if key == root.key():   # 찾는 키 = 조사중인 키
                break               # while 문 탈출 / 조사중인 key값이 찾는값으로 초기화되어있음
            
            elif key < root.key():  # 찾는 키 < 조사중인 키
                parent = root       # root노드를 부모노드
                root = root.left    # 조사중인 노드(키값)를 왼쪽으로 이동(자식노드)
            
            elif key > root.key():  # 찾는 키 > 조사중인 키
                parent = root       # root노드를 부모노드
                root = root.right   # 조사중인 노드(키값)를 오른쪽으로 이동(자식노드)
        #while 문 탈출
        return root, parent         # root의 key값이 찾는값으로 초기화된 상태 / parent는 root의 부모노드로 초기화된 상태

    def insert(self, key, value=None):  # 삽입 할 노드, 삽입 할 노드의 key값, 노드의 value값(이름)
        # 삽입 할 노드의 키값과 같은 키값을 갖는 노드를 찾게함  / 찾는노드와 찾는노드의 부모노드 return 됨
        node, parent = self.search_p(key)    
        #위 과정으로 삽입될 자리를 찾음(삽입될 노드의 부모가 결정됨)
        # 삽입 할 노드의 키값을가진 노드가 이미 존재하는 경우
        if node is not None:            
            if key == node.key():       # 존재하는 노드가 삽입할 노드의 key값
                node.set_value(value)   # 존재하는 노드의 value값을 업데이트 시킴
                return node
        # 삽입 할 노드의 키값을가진 노드가 존재하지 않는 경우(정상적으로 삽입가능)
        elif node is None:  # node 는 None / node의 부모 parent는 삽입할 노드의 부모노드로 설정됨
            new_node = Node(key,value)      # 삽입할 노드를 (객체) 생성
            
            if parent == None:              # node,parent 둘다 없는 경우 /백지에 추가하는것
                self.root = new_node
            
            elif key < parent.key():        # 삽입할 노드의 key 값 < 부모노드의 key
                parent.left = new_node
            
            elif key > parent.key():        # 삽입할 노드의 key 값 > 부모노드의 key
                parent.right = new_node
        
        return node
    
    def find_min_p(self, root, parent): # 노드와 노드의 부모
        while root.left is not None:    # 루트노드의 left 가 존재하는 동안 
            parent = root
            root = root.left
        return root, parent

    # def find_max_p(self, root, parent):  # 노드와 노드의 부모
    #     while root.right is not None:    # 루트노드의 right 가 존재하는 동안
    #         parent = root
    #         root = root.right
    #     return root
    
    def delete(self, key):          #key 값에 해당하는 노드를 삭제 / 노드의 자식과 노드의 부모를 연결
        # 삭제 할 노드의 키값과 같은 키값을 갖는 노드를 찾게함  / 찾는노드와 찾는노드의 부모노드 return 됨
        node, parent = self.search_p(key)
        # 삭제하려는 노드가 없으면
        if node is None:    
            return None
        # 삭제하려는 노드가 있으면
        elif node.left is None or node.right is None:   # 삭제하려는 노드의 자식의 갯수 1이하 
            if node.key() < parent.key():       # parent.left = node
                # 노드의 1개이하의 자식이 왼쪽인지 오른쪽인 결정
                child = node.left
                if node.right is not None:
                    child = node.right
                # 노드의 부모 왼쪽을 노드의 자식으로 초기화 
                parent.left = child
                
            elif parent.key() < node.key():     # parent.right = node
                parent.right = node.left
                # 노드의 1개이하의 자식이 왼쪽인지 오른쪽인 결정
                child = node.left
                if node.right is not None:
                    child = node.right
                # 노드의 부모 오른쪽을 노드의 자식으로 초기화
                parent.right = child
        # 삭제하려는 노드가 있으면
        else:       # 삭제하려는 노드의 자식의 갯수 = 2
            # 삭제한 후 대체할 노드를 (오른쪽 서브트리의 최솟값) 찾을거임  / 왼쪽 서브트리에서 찾는다면 (왼쪽 서브트리의 최대값찾기)
            if node.key() < parent.key():  # parent.left = node
                subMin, subMin_p = self.find_min_p(node.right, node)  # 오른쪽 서브트리의 최솟값
                parent.left = subMin                # (1)삭제할 노드의 부모노드의 왼쪽팔을 연결
                subMin.left = node.left             # (2)삭제할 노드의 자식들과의 링크를 대체할 노드로 연결
                subMin.right = node.right           # (2)삭제할 노드의 자식들과의 링크를 대체할 노드로 연결 
                subMin_p.left = None                # (3)대체할 노드와 대체할 노드의부모와 연결 끊기
            
            elif parent.key() < node.key():  # parent.right = node
                subMin = self.find_min_p(node.right, node)    # 오른쪽 서브트리의 최솟값
                parent.right = subMin               # (1)삭제할 노드의 부모노드의 오른쪽팔을 연결
                subMin.left = node.left             # (2)삭제할 노드의 자식들과의 링크를 대체할 노드로 연결
                subMin.right = node.right           # (2)삭제할 노드의 자식들과의 링크를 대체할 노드로 연결
                subMin_p.left = None                # (3)대체할 노드와 대체할 노드의부모와 연결 끊기
                
                
