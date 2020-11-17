import random
from util import Vertex
from util import Edge
from util import Graph
"""
You'll want to implement a smarter decision logic. This is skeleton code that you should copy and replace in your repository.
"""
class PercolationPlayer:

	def getEdges(graph, vertex):
	 	listofedges = []
	 	for edges in graph.E:
	 		if edge.v1 == vertex:
	 			listofedges.append(edge)
	 		elif edge.v2 == vertex:
	 			listofedges.append(edge)
	 	return listofedges

	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == -1
	def ChooseVertexToColor(graph, player):
		# maxEdges = 0
		# maxEdgeVertex = None
		# for vertex in list(graph.V):
		# 	if vertex.color == -1:
		# 		if len(getEdges(graph, vertex)) > maxEdges:
		# 			maxEdges = len(getEdges(graph, vertex))
		# 			maxEdgeVertex = vertex
		# return maxEdgeVertex
		return random.choice([v for v in graph.V if v.color == -1])


	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == player
	def ChooseVertexToRemove(graph, player):
		leastEdges = 10000	
		leastEdgeVertex = None
		for vertex in list(graph.V):
			if vertex.color == player:
				if len(getEdges(graph, vertex)) < leastEdges:
					leastEdges = len(getEdges(graph, vertex))
					leastEdgeVertex = vertex
		return leastEdgeVertex

# Feel free to put any personal driver code here.
def main():
    pass

if __name__ == "__main__":
    main()