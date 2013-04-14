class Stack():
	def __init__(self,n=5):
		self.a = [None]*n
		self.t = -1
		self.N = n
	
	def size(self):
		return self.t+1
	
	def isEmpty(self):
		return (self.t < 0)
		
	def push(self,o):
		if self.size() == self.N:
			raise OverflowError()
		self.t += 1
		self.a[self.t] = o
		
	def pop(self):
		if self.isEmpty():
			raise LookupError()
		o = self.a[self.t]
		self.t -= 1
		return o
	
	def top(self):
		if self.isEmpty():
			raise LookupError()
		return self.a[self.t]
		
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.isEmpty():
			raise StopIteration
		return self.pop()
		
	def __repr__(self):
		if self.isEmpty():
			return '<empty stack>'
		s = ''
		connector = ''
		for p in range(0, self.t+1):
			s += connector + str(self.a[p])
			connector = '->'
		return s

if __name__ == "__main__":		
	s = Stack()
	print('')
	print(s.isEmpty())
	print(s.size())
	print(s)

	s.push(6)
	s.push(5)
	s.push(7)
	s.push(9)
	s.push(10)
	print('')
	print(s.isEmpty())
	print(s.size())
	print(s.top())
	print(s)

	print('')
	print(s.pop())
	print(s.isEmpty())
	print(s.size())
	print(s.top())
	print(s)

	print('')
	print(s.pop())
	print(s.isEmpty())
	print(s.size())
	print(s.top())
	print(s)

	print('')
	print(s.pop())
	print(s.isEmpty())
	print(s.size())
	print(s.top())
	print(s)

	print('')
	print(s.pop())
	print(s.isEmpty())
	print(s.size())
	print(s.top())
	print(s)

	print('')
	print(s.pop())
	print(s.isEmpty())
	print(s.size())
	print(s)
