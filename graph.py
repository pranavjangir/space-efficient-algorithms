class Graph:
	# n is the vertex count
	# edges reprent a tupe (u, v) which means there is
	# an edge from u->v
	def __init__(self, n, edges, src):
		self.n = n
		for edge in edges:
			self.outdegree[edge[0]].append(edge[1])
			self.indegree[edge[1]].append(edge[0])
		for v in range(n):
			self.inptr[v] = 0
			self.outptr[v] =  0
		self.TOTAL_OPERATIONS = 0
		self.cur_vertex = src
		self.source = src

	def GetOutMinimum(self, v):
		cur_minm = 1e16
		for child in self.outdegree[v]:
			if (child < cur_minm):
				cur_minm = child
		return cur_minm

	def HasOutDegree(self, v):
		return (self.outdegree[v].length() > 0)

	def HasInDegree(self, v):
		return (self.indegree[v].length() > 0)

	def GetInMinimum(self, v):
		cur_minm = 1e16
		for parent in self.indegree[v]:
			if (parent < cur_minm):
				cur_minm = parent
		return cur_minm

	def CurInPtr(self, v):
		assert HasInDegree(v)

		return self.indegree[v][self.inptr[v]]

	def CurOutPtr(self, v):
		assert HasOutDegree(v)

		return self.outdegree[v][self.outptr[v]]

	def RotateInPtr(self, v):
		array_len = self.indegree[v].length()
		if (array_len > 0):
			self.inptr[v] = (self.inptr[v] + 1)%array_len 

	def RotateOutPtr(self, v):
		array_len = self.outdegree[v].length()
		if (array_len > 0):
			self.outdegree[v] = (self.outdegree[v] + 1)%array_len 

	def next_indegree_element(self, v):
		array_len = self.indegree[v].length()
		if (array_len > 0):
			return self.indegree[v][(self.inptr[v]+1)%array_len]


	def next_outdegree_element(self, v):
		array_len = self.outdegree[v].length()
		if (array_len > 0):
			return self.outdegree[v][(self.outptr[v]+1)%array_len]

	def Precompute(self):
		for v in range(self.n):
			if (HasInDegree(v)):
				indegree_minimum = GetInMinimum(v)
				while (CurInPtr(v) > indegree_minimum):
					RotateInPtr(v)
			if (HasOutDegree(v)):
				outdegree_minimum = GetOutMinimum(v)
				while (CurOutPtr(v) > outdegree_minimum):
					RotateOutPtr(v)

	# 0 means vertex is colored WHITE
	# 1 means vertex is colored BLACK			
	def GetColor(self, v):
		if (HasInDegree(v) and CurInPtr(v) != GetInMinimum(v)):
			return 1
		if (HasOutDegree(v) and CurOutPtr(v) != GetOutMinimum(v)):
			return 1
		return 0

	def BackTrack(self):
		if (self.source == self.cur_vertex):
			print("DFS complete!")
		else:
			old_vertex = self.cur_vertex
			self.cur_vertex = CurInPtr(self.cur_vertex)
			# Set the in degree head to something other than minimum element
			if (self.indegree[old_vertex].length > 1):
				if (CurInPtr(old_vertex) == GetInMinimum(old_vertex)):
					RotateInPtr(old_vertex)

	def GoForward(self):
		# Incomplete. Need to check the current out ptr and if it is 
		# white then we visit, otherwise we search for a white one.
		# We do this until we hit the minimum element again, at which point
		# we backtrack because it menas that there are no longer any white
		# vertices available.
		if (self.outdegree[self.cur_vertex].length() > 0):
			if (GetColor(CurOutPtr(v)) == 0):
				old_vertex = self.cur_vertex
				self.cur_vertex = CurOutPtr(v)

