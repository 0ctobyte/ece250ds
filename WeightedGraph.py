from MinPriorityQueue import MinPriorityQueue

inf = float("inf")
white, grey, black = range(3)

class Vertex():
	def __init__(self,value):
		self.value = value
		self.degree = 0
		self.d = 0
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
		s = str(self.value) + '(' + str(self.d) + '): '
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
		return other != None and (self.u == other.u or self.u == other.v) and (self.v == other.v or self.v == other.u) and self.w == other.w
		
	def __repr__(self):
		return "(" + str(self.u.value) + ', ' + str(self.v.value) + ', ' + str(self.w) + ')'
		
class WeightedGraph():
	def __init__(self):
		self.V = []
		self.E = []
	
	def edge_count(self):
		return len(self.E)
	
	def insert(self,m,n,w):
		u, v = self.V[self.V.index(m)], self.V[self.V.index(n)]
		if u.insert(v,w) and v.insert(u,w):
			self.E.append(Edge(u, v, w))
	
	def add(self,v):
		if v not in self.V:
			self.V.append(v)
	
	def delete(self,m,n):
		u, v = self.V[self.V.index(m)], self.V[self.V.index(n)]
		if u.delete(v):
			self.E.remove(Edge(u, v, u.weight(v)))
	
	def PrimJarnik(self):
		V = []
		E = []
		V.append(Vertex(self.V[0].value))
		while len(V) < len(self.V):
			mini = None
			for e in self.E:
				if (e.u in V or e.v in V) and (e.u not in V or e.v not in V):
					mini = e if mini == None or e.w < mini.w else mini
			x = V[V.index(mini.v if mini.v in V else mini.u)]
			y = Vertex(mini.u.value if mini.u not in V else mini.v.value)
			x.insert(y,mini.w), y.insert(x,mini.w)
			V.append(y), E.append(Edge(x,y,mini.w))
		G = WeightedGraph()
		G.V = V
		G.E = E
		return G

	def Kruskal(self):
		V = [[Vertex(self.V[i].value)] for i in range(len(self.V))]
		E = []
		S = []
		S[:] = self.E
		while len(S) > 0 and len(V) > 1:
			mini = None
			for i in range(len(S)):
				mini = i if mini == None or S[i].w < S[mini].w else mini
			e = S.pop(mini)
			tu = tv = None
			for i in range(len(V)):
				if e.u in V[i] and e.v in V[i]:
					tu = tv = None
					break
				elif e.u in V[i]:
					tu = i
				elif e.v in V[i]:
					tv = i
			if tu != None and tv != None:
				V[tu] += V[tv]
				x = V[tu][V[tu].index(e.u)]
				y = V[tu][V[tu].index(e.v)]
				x.insert(y,e.w), y.insert(x,e.w)
				E.append(Edge(x,y,e.w))
				V.pop(tv)
		V[:] = [v for tree in V for v in tree]
		G = WeightedGraph()
		G.V = V
		G.E = E
		return G
		
	def __repr__(self):
		s = ''
		for v in self.V:
			s += str(v) + '\n'
		s = s[:-1]
		return s
		
if __name__=="__main__":
	v = [Vertex('A'), Vertex('B'), Vertex('C'), Vertex('D'), Vertex('E'), Vertex('F'), Vertex('G'), Vertex('H')]
	G = WeightedGraph()
	for i in v:
		G.add(i)
	G.insert(v[0],v[1],6)
	G.insert(v[0],v[5],12)
	G.insert(v[1],v[5],5)
	G.insert(v[1],v[2],14)
	G.insert(v[1],v[3],7)
	G.insert(v[2],v[3],3)
	G.insert(v[3],v[4],10)
	G.insert(v[4],v[5],8)
	G.insert(v[4],v[7],15)
	G.insert(v[5],v[6],9)
	print(G)
	print(G.E)
	print("")
	H = G.PrimJarnik()
	print(H)
	print(H.E)
	H = G.Kruskal()
	print(H)
	print(H.E)
	