from Queue import Queue
from Stack import Stack
from string import ascii_lowercase
from random import randrange

inf = float("inf")
white, grey, black = range(3)

class Vertex():
	def __init__(self,value):
		self.value = value
		self.d = 0
		self.f = 0
		self.parent = None
		self.colour = None
		self.degree = 0
		self.adjacent = []
		
	def insert(self,u):
		if u in self.adjacent:
			return False
		self.adjacent.append(u)
		self.degree += 1
		return True
		
	def delete(self,u):
		if u not in self.adjacent:
			return False
		self.adjacent.remove(u)
		self.degree -= 1
		return True
		
	def __repr__(self):
		s = str(self.value) + ' (' + str(self.d) + ', ' + str(self.f) + ')' + ': '
		if len(self.adjacent) == 0:
			return s
		s += '['
		for u in self.adjacent:
			s += str(u.value) + ' '
		s = s[:-1]
		s += ']'
		return s
		
		
class Graph():
	def __init__(self,values):
		self.V = [Vertex(values[i]) for i in range(len(values))]
		self.edge_count = 0
	
	def insert(self,m,n):
		if self.V[n].insert(self.V[m]) and self.V[m].insert(self.V[n]):
			self.edge_count += 1
	
	def delete(self,m,n):
		if self.V[n].delete(self.V[m]) and self.V[m].delete(self.V[n]):
			self.edge_count -= 1
	
	def BreadthFirstSearch(self,s):
		q = Queue(len(self.V)+1)
		for v in self.V:
			v.d = inf
			v.colour = white
		self.V[0].colour = grey
		self.V[0].d = 0
		q.enqueue(self.V[0])
		for v in q:
			for u in v.adjacent:
				if u.colour == white:
					u.d = v.d + 1
					u.colour = grey
					if u.value == s:
						return u
					q.enqueue(u)
			v.colour = black
			
	def BreadthFirstTraversal(self):
		q = Queue(len(self.V)+1)
		for v in self.V:
			v.colour = white
			v.d = inf
			v.parent = None
		self.V[0].colour = grey
		self.V[0].d = 0
		q.enqueue(self.V[0])
		for v in q:
			for u in v.adjacent:
				if u.colour == white:
					u.colour = grey
					u.d = v.d + 1
					u.parent = v
					q.enqueue(u)
				elif u.colour == grey:
					self.delete(self.V.index(u),self.V.index(v))
			v.colour = black
	
	def DepthFirstSearch(self,r):
		s = Stack(len(self.V)+1)
		for v in self.V:
			v.parent = None
			v.colour = white
			v.d = v.f = inf
		time = 0
		s.push(self.V[0])
		while not s.isEmpty():
			v = s.top()
			if v.colour == white:
				v.colour = grey
				v.d = time = time+1
			for u in v.adjacent:
				if u.colour == white:
					u.parent = v
					s.push(u)
					break
			if u.colour != white:
				v.f = time = time+1
				v.colour = black
				if v.value == r:
					return v
				s.pop()
				
	def DepthFirstTraversal(self):
		s = Stack(len(self.V)+1)
		for v in self.V:
			v.parent = None
			v.colour = white
			v.d = v.f = inf
		time = 0
		s.push(self.V[0])
		while not s.isEmpty():
			v = s.top()
			if v.colour == white:
				v.colour = grey
				v.d = time = time+1
			for u in v.adjacent:
				if u.colour == white:
					u.parent = v
					s.push(u)
					break
				if u.parent != v and v.parent != u:
					self.delete(self.V.index(u),self.V.index(v))
			if u.colour != white:
				v.f = time = time+1
				v.colour = black
				s.pop()
		
	def __repr__(self):
		s = ''
		for v in self.V:
			s += str(v) + '\n'
		s = s[:-1]
		return s
		
if __name__=="__main__":
	#G = Graph([list(ascii_lowercase)[i] for i in range(10)])
	G = Graph(['A', 'S', 'B', 'D', 'C', 'G', 'E', 'F'])
	G.insert(0,1)
	G.insert(0,3)
	G.insert(1,2)
	G.insert(1,4)
	G.insert(2,4)
	G.insert(3,5)
	G.insert(4,6)
	G.insert(4,7)
	G.insert(5,6)
	print("\n"+str(G))
	u = G.BreadthFirstSearch('C')
	print("\n"+str(u))
	print("\n"+str(G))
	u = G.DepthFirstSearch('C')
	print("\n"+str(u))
	print("\n"+str(G))
	# G.BreadthFirstTraversal()
	# print("\n"+str(G))
	G.DepthFirstTraversal()
	print("\n"+str(G))
	
	