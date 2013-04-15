from MaxBinaryHeap import *

class MaxPriorityQueue():
	def __init__(self):
		self.A = []
	
	def peek(self):
		return self.A[0]
	
	def insert(self,key):
		self.A.append(key)
		i = len(self.A)-1
		while i > 0 and self.A[Parent(i)] < self.A[i]:
			self.A[Parent(i)], self.A[i] = self.A[i], self.A[Parent(i)]
			i = Parent(i)
	
	def extractMax(self):
		self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
		Heapify(self.A,0,len(self.A)-1)
		return self.A.pop()
		
	def rebuild(self):
		BuildHeap(self.A)
	
	def __iter__(self):
		return self
		
	def __next__(self):
		if len(self.A) == 0:
			raise StopIteration()
		return self.extractMax()
		
	def __repr__(self):
		return str(self.A)
		
if __name__=="__main__":
	a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	pq = MaxPriorityQueue()
	for i in a:
		pq.insert(i)
	print(pq)
	print(pq.extractMax())
	print(pq)