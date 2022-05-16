""" Node Class: storing (key, value) """
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


""" Binary Search Tree Class """
class BinarySearchTree:
	def __init__(self, root=None):
		self.root = root
	
	def search(self, key): # loop version
		root = self.root
		while root is not None:
			if key == root.key():
				break
			elif key < root.key():
				root = root.left
			elif key > root.key():
				root = root.right
		
		return root
	
	""" returns node holding key and its parent"""
	def search_p(self, key): 
		root, parent = self.root, None
		while root is not None:
				if key == root.key(): # 첮음
					break
				elif key < root.key(): #왼쪽으로 
					parent = root
					root = root.left
				elif key > root.key(): #오른쪽으로
					parent = root
					root = root.right
		return root, parent
	
	def insert(self, key, value=None):
		node, p = self.search_p(key)
		if node is not None and k==node.key():
			node.set_value(value)
			return node
		
		new_node = Node(key, value)
		if p is None:
			self.root = new_node
		elif key < p.key():
			p.left = new_node
		else:
			p.right = new_node
		
		return node
	
	""" replace <node> with <rep_node> """ 
	# p: parent of <node>
	# rep_p: parent of <rep_node>
	def replace(self, node, rep_node, p, rep_p): 
		# A. REPLACE p-to-node link
		# case-1: node is root (p is None)
		if p is None: 
			self.root = rep_node
		# case-2: node is p.left
		elif node == p.left:
			p.left = rep_node
		# case-3: node is p.right
		else :
			p.right = rep_node
		
		# B. REPLACE node-to-child(s) link(s) IF <rep_node> exists
		# case-1: <rep_node> is <node>'s left child  --> Do nothing
		
		if rep_node == p.left:
			pass
		# case-2: <rep_node> is <node>'s right child --> replace the left link IF node.left exists
		
		elif rep_node == p.right:
			p.left = rep_node
		# case-3: <rep_node> is not <node>'s child --> replace both left and right links
		else :
			p.left = rep_node; p.right = rep_node
		
		# C. DELETE <rep_p> to <rep_node> link (already coded below)
		rep_p.left = None
			
	def find_min_p(self, root, p):
		while root.left is not None:
			p = root
			root = root.left
		return root, p
		
	def delete(self, key):
		node, p = self.search_p(key)
		if node is None:
			return node
		
		# number of children <= 1
		elif node.left is None or node.right is None:
			# determine the child (left or right?)
			child = node.left
			if node.right is not None: child = node.right
			# replace <node> with <child>
			self.replace(node, child, p, node)
		
		# number of children == 2
		else:
			# find minimum key from the right subtree
			right_min, right_min_p = self.find_min_p(node.right, node)
			# replace <node> with <right_min>
			self.replace(node, right_min, p, right_min_p)
			
		return node
	
	def preorder(self, root):
		if root is not None:
			print(root.key(), end=" ")
			self.preorder(root.left)
			self.preorder(root.right)
	
	def postorder(self, root):
		if root is not None:
			self.postorder(root.left)
			self.postorder(root.right)
			print(root.key(), end=" ")
	
	def inorder(self, root):
		if root is not None:
			self.inorder(root.left)
			print(root.key(), end=" ")
			self.inorder(root.right)
	
	
