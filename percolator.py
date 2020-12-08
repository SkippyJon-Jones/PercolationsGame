import random
from util import Vertex
from util import Edge
from util import Graph
"""
You'll want to implement a smarter decision logic. This is skeleton code that you should copy and replace in your repository.
"""

# Gets the edges attached to a given vertex
def getEdges(graph, vertex):
 	listofedges = []
 	for edge in graph.E:
 		if edge.a == vertex:
 			listofedges.append(edge)
 		elif edge.b == vertex:
 			listofedges.append(edge)
 	return listofedges

# Gets the other vertex on an edge from a given edge and vertex
def getOtherVertex(edge, vertex):
	if edge.a == vertex:
		return edge.b
	else:
		return edge.a

class PercolationPlayer:


	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == -1
	def ChooseVertexToColor(graph, player):
		bestvertex = None
		maxdegreevertex = -100

		# This loop finds the highest degree vertex in the graph that has at least
		#  one edge connected to an ally vertex
		for vertex in graph.V:
			if vertex.color == -1:
				degreevertex = len(getEdges(graph, vertex))
				valid = False
				for edge in getEdges(graph, vertex):
					if getOtherVertex(edge, vertex).color == player or getOtherVertex(edge,vertex).color != -1:
						degreevertex-=1
						if getOtherVertex(edge, vertex).color == player:
							valid = True
				if degreevertex >= maxdegreevertex and valid == True:
					maxdegreevertex = degreevertex
					bestvertex = vertex

		# If there was no vertex that had an edge connecting to at least one
		#  ally vertex then bestvertex == None is true and the function instead returns the 
		#  vertex with the highest number of edges
		if bestvertex == None:
			maxEdges = 0
			maxEdgeVertex = None
			for vertex in graph.V:
				if vertex.color == -1:
					if len(getEdges(graph, vertex)) >= maxEdges:
						maxEdges = len(getEdges(graph, vertex))
						maxEdgeVertex = vertex
			return maxEdgeVertex

		# As long as bestvertex isn't none, it is returned
		return bestvertex


	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == player
	def ChooseVertexToRemove(graph, player):
		
		mindifference = -100000000000
		bestvertex = None
		
		# Loops through the graph and keeps track of the "score" of each
		#  vertex in the graph, adding it to a list
		vertices = []
		for vertex in graph.V:
			if vertex.color == player:
				# This check insures that the function returns any obvious wins
				if getEdges(graph, vertex) == list(graph.E):
					return vertex
				opponentvertices = 0
				allyvertices = 0
				for edge in getEdges(graph, vertex):
					if getOtherVertex(edge, vertex).color != player:
						opponentvertices+=1
					else:
						allyvertices+=1

				vertices.append(opponentvertices - allyvertices)


		# sorts the list in ascending order
		vertices.sort()

		# if the highest score of any vertex is less than 0
		# 	the function designates the best vertex as the vertex with
		#  	the highest score
		if vertices[len(vertices) - 1] < 0:
			maxdifference = -10000000
			for vertex in graph.V:
				if vertex.color == player:
					if getEdges(graph, vertex) == list(graph.E):
						return vertex
					opponentvertices = 0
					allyvertices = 0
					for edge in getEdges(graph, vertex):
						if getOtherVertex(edge, vertex).color != player:
							opponentvertices+=1
						else:
							allyvertices+=1

					if (opponentvertices - allyvertices) >= maxdifference:
						maxdifference = opponentvertices - allyvertices
						bestvertex = vertex
		# Otherwise, the function designates the vertex with the score closest to
		#  0 from the positive side as the best vertex
		else:
			maxdifference = 10000000
			for vertex in graph.V:
				if vertex.color == player:
					if getEdges(graph, vertex) == list(graph.E):
						return vertex
					opponentvertices = 0
					allyvertices = 0
					for edge in getEdges(graph, vertex):
						if getOtherVertex(edge, vertex).color != player:
							opponentvertices+=1
						else:
							allyvertices+=1

					if (opponentvertices - allyvertices) < maxdifference and (opponentvertices - allyvertices) >= 0:
						maxdifference = opponentvertices - allyvertices
						bestvertex = vertex
								
		return bestvertex

# Feel free to put any personal driver code here.
def main():
    pass

if __name__ == "__main__":
    main()