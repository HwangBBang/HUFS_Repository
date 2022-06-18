#Tree

class Node:
    def __init__(self, item = None, left = None, right = None):
        self.item = item ;self.left = left;self.right = right


def preorder(root):             #self -> left -> right
    if root is not None:
        print(root.item, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):              #left -> self -> right
    if root is not None:
        inorder(root.left)
        inorder(root.item, end=" ")
        inorder(root.right)

def postorder(root):            #left -> right -> self
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.item, end = " ")
        
def search(root, x):
    if root is None:            #노드(노드)가 아예 없다면
        return None
    if root.item == x:          #노드의 아이템(키) 값이 찾는 x라면 
        return root             #해당노드를 반환
    node = None                 #node라는 변수 생성및 초기화
    node = search(root.left, x)
    if node is not None:
        return node
    node = search(root.rigjt, x)    
    return node

def insert_simple(p, side, x):
    global root
    if root is None:            
        root = Node(x)          #root라는 객체 생성
    else:                       #root가 있다면
        node_p =search(root, p) #찾아서 node_p라고 정의 
        if node_p is None:
            return None
        if side == 'left':
            node_p.left = Node(x)#node_p의 왼쪽 자식노드를 객체로생성
        else:
            node_p.right = Node(x)#node_p의 오른쪽 자식노드를 객체로생성

def size(root):                 #트리의 모든 노드의 갯수
    if root is None:
        return 0
    else:
        result = size(root.left)+size(root.right)
        return result

def height(root):               #깊이중 최댓값
    if root is None:   
        return -1               #노드가 없으면 -1
    else:
        result = max(height(root.left), height(root.right)) + 1
        return result