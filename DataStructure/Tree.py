class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item, self.left, self.right = item, left, right

    def preorder(root):
        if root is not None:
            print(root.item, end=" ")
            preorder(root.left)
            preorder(root.right)

    def inorder(root):
        if root is not None:
            inorder(root.left)
            print(root.item, end=" ")
            inorder(root.right)

    def postorder(root):
        if root is not None:
            postorder(root.left)
            postorder(root.right)
            print(root.item, end=" ")

    def search(root, x):
        if root is None:
            return None
        if root.item == x:
            return root
        node = None
        if root.left:
            node = search(root.left,x)
        if node is not None:
            return node
        if root.right: 
            node = search(root.right, x)
        return node

    def insert_simple(p, side, x):
        global root
        if root is None:
            root = Node(x)
        else:
            node_p = search(root, p)
        if node_p is None: 
            return None
        if side=='left':
            node_p.left = Node(x)
        else:
            node_p.right = Node(x)

    def size(root):
        if root is None:
            return 0
        else:
            return 1+size(root.left)+size(root.right)

    def height(root):
        if root is None:
            return -1
        elif root.left is None and root.right is None:
            return 0
        else:
            result = max(height(root.left)+1,height( root.right)+1)
            return result


root = None

while True:
    cmd = input()
    if cmd=='exit':
        break
    elif cmd=='preorder':
        preorder(root); print();
    elif cmd=='postorder':
        postorder(root); print();
    elif cmd=='inorder':
        inorder(root); print();
    elif cmd=='size':
        print(size(root))
    elif cmd=='height':
        print(height(root))
    else:
        cmd = cmd.split()
        if cmd[0]=='search':
            val = cmd[1]
            node = search(root, int(val))
            if node is None: print(val+' not found')
            else: print(val+' found') 
        elif cmd[0]=='insert':
            p, side, val = cmd[1:]
            insert_simple(int(p), side, int(val))
