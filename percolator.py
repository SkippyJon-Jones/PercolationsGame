import random
from util import Vertex
from util import Edge
from util import Graph
"""
You'll want to implement a smarter decision logic. This is skeleton code that you should copy and replace in your repository.
"""

def getEdges(graph, vertex):
 	listofedges = []
 	for edge in graph.E:
 		if edge.a == vertex:
 			listofedges.append(edge)
 		elif edge.b == vertex:
 			listofedges.append(edge)
 	return listofedges

def getOtherVertex(edge, vertex):
	if edge.a == vertex:
		return edge.b
	else:
		return edge.a

class PercolationPlayer:


	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == -1
	def ChooseVertexToColor(graph, player):
		maxEdges = 0
		maxEdgeVertex = None
		for vertex in list(graph.V):
			if vertex.color == -1:
				if len(getEdges(graph, vertex)) >= maxEdges:
					maxEdges = len(getEdges(graph, vertex))
					maxEdgeVertex = vertex
		return maxEdgeVertex
		# return random.choice([v for v in graph.V if v.color == -1])


	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == player
	def ChooseVertexToRemove(graph, player):
		mostbadvertices = 0
		bestvertex = None

		mostgoodvertices = 100000
		for vertex in graph.V:
			if vertex.color == player:
				badvertices = 0
				goodvertices = 0
				for edge in getEdges(graph, vertex):
					if getOtherVertex(edge, vertex).color != player:
						badvertices+=1
					else:
						goodvertices+=1
				if badvertices >= mostbadvertices and goodvertices < mostgoodvertices:
					mostbadvertices = badvertices
					mostgoodvertices = goodvertices
					bestvertex = vertex

		return bestvertex



# Feel free to put any personal driver code here.
def main():
    pass

if __name__ == "__main__":
    main()