class Queue():
	def __init__(self,n=5):
		self.N = n;
		self.a = [None] * n
		self.f = self.r = 0
	
	def size(self):
		return (self.N+(self.r-self.f)) % self.N
	
	def isEmpty(self):
		return (self.size() == 0)
	
	def front(self):
		if self.isEmpty():
			raise LookupError()
		return self.a[self.f]
	
	def enqueue(self,o):
		if self.size() == self.N-1:
			raise OverflowError
		self.a[self.r] = o
		self.r = (self.r+1) % self.N
	
	def dequeue(self):
		if self.isEmpty():
			raise LookupError();
		o = self.a[self.f]
		self.f = (self.f+1) % self.N
		return o
		
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.isEmpty():
			raise StopIteration
		return self.dequeue()
	
	def __repr__(self):
		if self.isEmpty():
			return '<empty queue>'
		s = ''
		connector = ''
		p = self.f
		while p != self.r:
			s += connector + str(self.a[p])
			connector = '<-'
			p = (p+1) % self.N
		return s

if __name__ == "__main__":
	q = Queue(6)
	print('')
	print(q.isEmpty())
	print(q.size())
	print(q)

	q.enqueue(6)
	q.enqueue(5)
	q.enqueue(7)
	q.enqueue(9)
	q.enqueue(10)
	print('')
	print(q.isEmpty())
	print(q.size())
	print(q.front())
	print(q)

	print('')
	print(q.dequeue())
	print(q.isEmpty())
	print(q.size())
	print(q.front())
	print(q)

	print('')
	print(q.dequeue())
	print(q.isEmpty())
	print(q.size())
	print(q.front())
	print(q)

	print('')
	print(q.dequeue())
	print(q.isEmpty())
	print(q.size())
	print(q.front())
	print(q)

	print('')
	print(q.dequeue())
	print(q.isEmpty())
	print(q.size())
	print(q.front())
	print(q)

	print('')
	print(q.dequeue())
	print(q.isEmpty())
	print(q.size())
	print(q)