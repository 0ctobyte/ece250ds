from MinPriorityQueue import MinPriorityQueue
from Stack import Stack

inf = float("inf")
white, grey, black = range(3)

class Vertex():
	def __init__(self,value):
		self.value = value
		self.degree = 0
		self.d = 0
		self.f = 0
		self.colour = None
		self.parent = None
		self.adjacent = []
		self.weights = []
		
	def insert(self,u,w):
		if u in self.adjacent:
			self.weights[self.adjacent.index(u)] = w
			return True
		self.adjacent.append(u)
		self.weights.append(w)
		self.degree += 1
		return True
		
	def delete(self,u):
		if u not in self.adjacent:
			return False
		self.weights.pop(self.adjacent.index(u))
		self.adjacent.remove(u)
		self.degree -= 1
		return True
		
	def weight(self,u):
		if u in self.adjacent:
			return self.weights[self.adjacent.index(u)]
	
	def __eq__(self,other):
		return other != None and self.value == other.value
	
	def __ne__(self,other):
		return other == None or self.value != other.value
		
	def __lt__(self,other):
		return other != None and self.d < other.d
	
	def __le__(self,other):
		return other != None and self.d <= other.d
	
	def __gt__(self,other):
		return other != None and self.d > other.d
	
	def __ge__(self,other):
		return other != None and self.d >= other.d
	
	def __repr__(self):
		s = str(self.value) + '(' + str(self.d) + ', ' + str(self.f) + '): '
		if len(self.adjacent) == 0:
			return s
		s += '['
		for i in range(len(self.adjacent)):
			s += str(self.adjacent[i].value) + '(' + str(self.weights[i]) + ') '
		s = s[:-1]
		s += ']'
		return s

class Edge():
	def __init__(self,u,v,w):
		self.u = u
		self.v = v
		self.w = w
		
	def __eq__(self,other):
		return other != None and (self.u == other.u) and (self.v == other.v) and self.w == other.w
		
	def __repr__(self):
		return "(" + str(self.u.value) + ', ' + str(self.v.value) + ', ' + str(self.w) + ')'
		
class WeightedDigraph():
	def __init__(self):
		self.V = []
		self.E = []
	
	def edge_count(self):
		return len(self.E)
	
	def insert(self,m,n,w):
		u, v = self.V[self.V.index(m)], self.V[self.V.index(n)]
		if u.insert(v,w):
			self.E.append(Edge(u, v, w))
	
	def add(self,v):
		if v not in self.V:
			self.V.append(v)
	
	def delete(self,m,n):
		u, v = self.V[self.V.index(m)], self.V[self.V.index(n)]
		if u.delete(v):
			self.E.remove(Edge(u, v, u.weight(v)))
	
	def Dijkstra(self):
		q = MinPriorityQueue()
		for v in self.V:
			v.d = inf
			v.parent = None
			v.colour = white
		self.V[0].d = 0
		self.V[0].colour = grey
		q.insert(self.V[0])
		for v in q:
			for u, w in zip(v.adjacent,v.weights):
				if u.colour != black:
					if u.d > v.d + w:
						u.d = v.d + w
						u.parent = v
						q.rebuild()
					if u.colour == white:
						u.colour = grey
						q.insert(u)
			v.colour = black
			
	def BellmanFord(self):
		for v in self.V:
			v.d = inf
			v.parent = None
		self.V[0].d = 0
		for i in range(len(self.V)-1):
			for e in self.E:
				if e.v.d > e.u.d + e.w:
					e.v.d = e.u.d + e.w
					e.v.parent = e.u
		for e in self.E:
			if e.v.d > e.u.d + e.w:
				return False
		return True
		
	def TopologicalSort(self):
		s = Stack(len(self.V)+1)
		S = []
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
				S.insert(0,v)
				s.pop()
		return S
		
	def __repr__(self):
		s = ''
		for v in self.V:
			s += str(v) + '\n'
		s = s[:-1]
		return s
		
if __name__=="__main__":
	v = [Vertex('S'), Vertex('U'), Vertex('V'), Vertex('X'), Vertex('Y')]
	G = WeightedDigraph()
	for i in v:
		G.add(i)
	G.insert(v[0],v[1],10)
	G.insert(v[0],v[3],5)
	G.insert(v[1],v[2],1)
	G.insert(v[1],v[3],2)
	G.insert(v[2],v[4],4)
	G.insert(v[3],v[2],9)
	G.insert(v[3],v[1],3)
	G.insert(v[3],v[4],2)
	G.insert(v[4],v[0],7)
	G.insert(v[4],v[2],6)
	print(G)
	print(G.E)
	print("")
	G.Dijkstra()
	print(G)
	print("-----------------------------------------")
	
	v = [Vertex('S'), Vertex('U'), Vertex('V'), Vertex('X'), Vertex('Y')]
	G = WeightedDigraph()
	for i in v:
		G.add(i)
	G.insert(v[0],v[1],10)
	G.insert(v[0],v[3],5)
	G.insert(v[1],v[2],1)
	G.insert(v[1],v[3],2)
	G.insert(v[3],v[2],9)
	G.insert(v[3],v[4],2)
	G.insert(v[4],v[2],6)
	print(G.TopologicalSort())
	print("-----------------------------------------")
	
	v = [Vertex('S'), Vertex('T'), Vertex('X'), Vertex('Y'), Vertex('Z')]
	G = WeightedDigraph()
	for i in v:
		G.add(i)
	G.insert(v[0],v[1],6)
	G.insert(v[0],v[3],7)
	G.insert(v[1],v[2],5)
	G.insert(v[1],v[3],8)
	G.insert(v[1],v[4],-4)
	G.insert(v[2],v[1],-2)
	G.insert(v[3],v[2],-3)
	G.insert(v[3],v[4],9)
	G.insert(v[4],v[0],2)
	G.insert(v[4],v[2],7)
	print(G)
	print(G.E)
	print("")
	print(G.BellmanFord())
	print(G)
	