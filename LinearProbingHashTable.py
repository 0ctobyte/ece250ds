class LinearProbingHashTable():
	def __init__(self,n=10):
		self.N = n
		self.a = [None] * n
		self.count = 0;
	
	def h(self,x,i):
		return ((hash(x)+i) % self.N)
	
	def size(self):
		return self.count
	
	def capacity(self):
		return self.N
	
	def loadFactor(self):
		return (self.count/self.N)
	
	def isEmpty(self):
		return (self.count == 0)
	
	def insert(self,x):
		if self.size() == self.N:
			raise OverflowError()
		i = 0
		probe = self.h(x,i)
		while self.a[probe] != None:
			i += 1
			probe = self.h(x,i)
		self.a[probe] = x
		self.count += 1
		
	def delete(self,x):
		for i in range(0, self.N):
			probe = self.h(x,i)
			if self.a[probe] == x:
				self.a[probe] = None
				self.count -= 1
				break;
	
	def member(self,x):
		for i in range(0, self.N):
			probe = self.h(x,i)
			if self.a[probe] == x:
				return True
		return False
		
	def __repr__(self):
		if self.isEmpty():
			return '<empty hash>'
		s = ''
		for i in range(0, self.N):
			s += str(i) + ': ' + str(self.a[i])
			s += '\n'
		return s[:-1]
			

if __name__ == "__main__":
	ht = LinearProbingHashTable()
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print(ht)
	
	ht.insert(3171)
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print('member: ' + str(ht.member(3171)))
	print(ht)
	
	ht.insert(4123)
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print('member: ' + str(ht.member(4123)))
	print(ht)
	
	ht.insert(5973)
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print('member: ' + str(ht.member(5973)))
	print(ht)
	
	ht.insert(2699)
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print('member: ' + str(ht.member(2699)))
	print(ht)
	
	ht.insert(5344)
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print('member: ' + str(ht.member(5344)))
	print(ht)
	
	ht.insert(5879)
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print('member: ' + str(ht.member(5879)))
	print(ht)
	
	ht.insert(9789)
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print('member: ' + str(ht.member(9789)))
	print(ht)
	
	ht.delete(5973)
	print('')
	print('empty: ' + str(ht.isEmpty()))
	print('size: ' + str(ht.size()))
	print('capacity: ' + str(ht.capacity()))
	print('load factor: ' + str(ht.loadFactor()))
	print('member: ' + str(ht.member(5973)))
	print(ht)