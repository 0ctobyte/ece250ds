class LinkedListNode():
	def __init__(self,value):
		self.value = value
		self.next = None
		self.prev = None
	
	def __repr__(self):
		return str(self.value)


class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0
	
	def size(self):
		return self.count
	def isEmpty(self):
		return (self.count == 0)
	
	def first(self):
		if self.isEmpty():
			raise LookupError()
		return self.head
	
	def last(self):
		if self.isEmpty():
			raise LookupError()
		return self.tail
	
	def prepend(self,p):
		newNode = LinkedListNode(p)
		newNode.next = self.head
		self.head = newNode
		if self.isEmpty():
			self.tail = newNode
		else:
			newNode.next.prev = newNode
		self.count += 1
		
	def append(self,p):
		newNode = LinkedListNode(p)
		newNode.prev = self.tail
		self.tail = newNode
		if self.isEmpty():
			self.head = newNode
		else:
			newNode.prev.next = newNode
		self.count += 1
		
	def remove(self,p):
		current = self.head
		while current != None and current.value != p:
			current = current.next
		if current == None:
			raise LookupError()
		if current == self.head and current == self.tail:
			self.head = self.tail = current.next = current.prev = None
		elif current == self.head:
			self.head = current.next
			self.head.prev = current.next = current.prev = None
		elif current == self.tail:
			self.tail = current.prev
			self.tail.next = current.next = current.prev = None
		else:
			current.prev.next = current.next
			current.next.prev = current.prev
			current.next = current.prev = None
		self.count -= 1
			
	def __repr__(self):
		if self.isEmpty():
			return '<empty list>'
		s = ''
		current = self.head
		connector = ''
		while current != None:
			s += connector + current.__repr__()
			connector = '->'
			current = current.next
		return s

if __name__ == "__main__":
	l = LinkedList()
	print('')
	print(l.isEmpty())
	print(l.size())
	print(l)

	l.prepend(6)
	l.append(5)
	l.append(7)
	l.prepend(9)
	l.append(10)
	print('')
	print(l.isEmpty())
	print(l.size())
	print(l.first())
	print(l.last())
	print(l)

	l.remove(10)
	print('')
	print(l.isEmpty())
	print(l.size())
	print(l.first())
	print(l.last())
	print(l)

	l.remove(9)
	print('')
	print(l.isEmpty())
	print(l.size())
	print(l.first())
	print(l.last())
	print(l)

	l.remove(5)
	print('')
	print(l.isEmpty())
	print(l.size())
	print(l.first())
	print(l.last())
	print(l)

	l.remove(6)
	print('')
	print(l.isEmpty())
	print(l.size())
	print(l.first())
	print(l.last())
	print(l)

	l.remove(7)
	print('')
	print(l.isEmpty())
	print(l.size())
	print(l)
