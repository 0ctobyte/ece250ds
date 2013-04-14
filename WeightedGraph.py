inf = float("inf")
white, grey, black = range(3)

class Vertex():
	def __init__(self,value):
		self.value = value
		self.degree = 0
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
	
	def __eq__(self,other):
		return other != None and self.value == other.value
		
	def __repr__(self):
		s = str(self.value) + ': '
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
	def __init__(self,values=[None]):
		self.V = [Vertex(values[i]) for i in range(len(values))]
		self.E = []
	
	def edge_count(self):
		return len(self.E)
	
	def insert(self,m,n,w):
		if self.V[n].insert(self.V[m],w) and self.V[m].insert(self.V[n],w):
			self.E.append(Edge(self.V[m], self.V[n], w))
	
	def delete(self,m,n):
		e = Edge(self.V[m], self.V[n], self.V[m].weights[self.V[m].adjacent.index(self.V[n])])
		if self.V[n].delete(self.V[m]) and self.V[m].delete(self.V[n]):
			self.E.remove(e)
			
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
		
		
	def __repr__(self):
		s = ''
		for v in self.V:
			s += str(v) + '\n'
		s = s[:-1]
		return s
		
if __name__=="__main__":
	G = WeightedGraph(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
	G.insert(0,1,6)
	G.insert(0,5,12)
	G.insert(1,5,5)
	G.insert(1,2,14)
	G.insert(1,3,7)
	G.insert(2,3,3)
	G.insert(3,4,10)
	G.insert(4,5,8)
	G.insert(4,7,15)
	G.insert(5,6,9)
	print(G)
	print(G.E)
	print("")
	H = G.PrimJarnik()
	print(H)
	print(H.E)
	