class BinarySearchTreeNode():
	def __init__(self,value):
		self.key = value
		self.right = self.left = self.parent = None
		
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
				self.right = BinarySearchTreeNode(x)
				self.right.parent = self
		else:
			if self.left != None:
				return self.left.insert(x)
			else:
				self.left = BinarySearchTreeNode(x)
				self.left.parent = self
		return True		

	def __repr__(self):
		return str(self.key)

class BinarySearchTree():
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
		
	def successor(self):
		if self.isEmpty():
			return None
		return self.root.successor()
		
	def predecessor(self):
		if self.isEmpty():
			return None
		return self.root.predecessor()
	
	def search(self,x):
		if self.isEmpty():
			return None
		return self.root.search(x)
	
	def insert(self,x):
		if self.isEmpty():
			self.root = BinarySearchTreeNode(x)
			self.count += 1
		elif self.root.insert(x):
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
