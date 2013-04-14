class AvlTreeNode():
	def __init__(self,value):
		self.key = value
		self.right = self.left = self.parent = None
	
	def isViolating(self):
		r = -1 if self.right == None else self.right.height()
		l = -1 if self.left == None else self.left.height()
		return (abs(l-r) > 1)
		
	def isBalanced(self):
		if self.right == None and self.left == None:
			return not self.isViolating()
		r = l = True
		if self.left != None:
			r = self.left.isBalanced()
		if self.right != None:
			l = self.right.isBalanced()
		return r and l and not self.isViolating()

	def sum(self):
		sum = self.key
		if self.right != None:
			sum += self.right.sum()
		if self.left != None:
			sum += self.left.sum()
		return sum
	
	def min(self):
		return self.left.min() if self.left != None else self
	
	def max(self):
		return self.right.max() if self.right != None else self
		
	def height(self):
		if self.right == None and self.left == None:
			return 0
		r = l = 0
		if self.right != None:
			r = self.right.height()
		if self.left != None:
			l = self.left.height()
		return 1 + max(r, l)
		
	def successor(self):
		if self.right != None:
			return self.right.min()
		parent = self.parent
		while parent != None and parent.key < self.key:
			parent = parent.parent
		return parent
		
	def predecessor(self):
		if self.left != None:
			return self.left.max()
		parent = self.parent
		while parent != None and parent.key > self.key:
			parent = parent.parent
		return parent
	
	def search(self,x):
		if x == self.key:
			return self
		elif x > self.key:
			return self.right.search(x) if self.right != None else None
		else:
			return self.left.search(x) if self.left != None else None
	
	def insert(self,x):
		if x == self.key:
			return False
		elif x > self.key:
			if self.right != None:
				return self.right.insert(x)
			else:
				self.right = AvlTreeNode(x)
				self.right.parent = self
		else:
			if self.left != None:
				return self.left.insert(x)
			else:
				self.left = AvlTreeNode(x)
				self.left.parent = self
		return True		

	def __repr__(self):
		return str(self.key)

class AvlTree():
	def __init__(self):
		self.root = None
		self.count = 0
		
	def isEmpty(self):
		return (self.count == 0)
	
	def size(self):
		return self.count
		
	def sum(self):
		if self.isEmpty():
			return 0
		return self.root.sum()
		
	def min(self):
		if self.isEmpty():
			return None
		return self.root.min()
	
	def max(self):
		if self.isEmpty():
			return None
		return self.root.max()
	
	def height(self):
		if self.isEmpty():
			return None
		return self.root.height()
		
	def successor(self):
		if self.isEmpty():
			return None
		return self.root.successor()
		
	def predecessor(self):
		if self.isEmpty():
			return None
		return self.root.predecessor()
		
	def isBalanced(self):
		if self.isEmpty():
			return None
		return self.root.isBalanced()
	
	def findViolatingNode(self,startingNode):
		parent = startingNode
		while parent != None:
			if parent.isViolating():
				break
			parent = parent.parent
		return parent
	
	def singleRightRotation(self,v):
		a = v.parent
		l = v.left
		l.parent = a
		v.parent = l
		l.right = v
		v.left = None
		if a != None:
			if v.key > a.key:
				a.right = l
			else:
				a.left = l
		else:
			self.root = l

	def singleLeftRotation(self,v):
		a = v.parent
		l = v.right
		l.parent = a
		v.parent = l
		l.right = v
		v.right = None
		if a != None:
			if v.key > a.key:
				a.right = l
			else:
				a.left = l
		else:
			self.root = l
		
	def rebalance(self,v,i):
		if v.left != None and v.left.left == i:
			self.singleRightRotation(v)
		elif v.right != None and v.right.right == i:
			self.singleLeftRotation(v)
	
	def search(self,x):
		if self.isEmpty():
			return None
		return self.root.search(x)
	
	def insert(self,x):
		if self.isEmpty():
			self.root = AvlTreeNode(x)
			self.count += 1
		elif self.root.insert(x):
			i = self.search(x)
			v = self.findViolatingNode(i)
			if v != None:
				self.rebalance(v,i)
			self.count += 1
		
	def delete(self,x):
		if not self.isEmpty():
			z = self.search(x)
			if z != None:
				y = z if z.left == None or z.right == None else z.successor()
				if y.left != None:
					x = y.left
				else:
					x = y.right
				if x != None:
					x.parent = y.parent
				if y.parent == None:
					 self.root.key = x.key
				else:
					if y == y.parent.left:
						y.parent.left = x
					else:
						y.parent.right = x
				z.key = y.key if y != z else z.key

if __name__=="__main__":
	from BinarySearchTreeAlgorithms import *
	avl = AvlTree()
	avl.insert(3)
	print(avl.isBalanced())
	avl.insert(2)
	print(avl.isBalanced())
	avl.insert(1)
	print(avl.isBalanced())
	print(avl.root)
	avl.insert(4)
	print(avl.isBalanced())
	print(avl.root)
	avl.insert(5)
	print(avl.isBalanced())
	print(avl.root)
	avl.insert(6)
	print(avl.isBalanced())
	print(avl.root)
	print(avl.height())
	print(str(avl.root.left.height()) + ' vs ' + str(avl.root.right.height()))
