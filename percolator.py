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
		# maxEdges = 0
		# maxEdgeVertex = None
		# for vertex in graph.V:
		# 	if vertex.color == -1:
		# 		if len(getEdges(graph, vertex)) >= maxEdges:
		# 			maxEdges = len(getEdges(graph, vertex))
		# 			maxEdgeVertex = vertex
		# return maxEdgeVertex

		# bestvertex = None
		# difference = -1000
		# for vertex in graph.V:
		# 	if vertex.color == -1:
		# 		allyvertices = 0
		# 		opponentvertices = 0
		# 		for edge in getEdges(graph, vertex):
		# 			if getOtherVertex(edge, vertex) == player or getOtherVertex(edge, vertex) == -1:
		# 				allyvertices+=1
		# 			else:
		# 				opponentvertices+=1
		# 		if allyvertices - opponentvertices >= difference:
		# 			difference = allyvertices - opponentvertices
		# 			bestvertex = vertex
		# return bestvertex

		# bestvertex = None
		# leastallyvertices = 0
		# for vertex in graph.V:
		# 	if vertex.color == -1:
		# 		allyvertices = 0
		# 		opponentvertices = 0
		# 		for edge in getEdges(graph, vertex):
		# 			if getOtherVertex(edge, vertex) == player:
		# 				allyvertices+=1
		# 			else:
		# 				opponentvertices+=1
		# 		if opponentvertices - allyvertices >= difference:
		# 			difference = opponentvertices - allyvertices
		# 			bestvertex = vertex
		# return bestvertex

		bestvertex = None
		maxdegreevertex = -100
		for vertex in graph.V:
			if vertex.color == -1:
				degreevertex = len(getEdges(graph, vertex))
				valid = False
				for edge in getEdges(graph, vertex):
					if getOtherVertex(edge, vertex).color == player or getOtherVertex(edge,vertex).color != -1:
						degreevertex-=1
						if getOtherVertex(edge, vertex).color == player:
							valid = True
				if (degreevertex >= maxdegreevertex and valid == True):
					maxdegreevertex = degreevertex
					bestvertex = vertex
			elif vertex.color == player:
				pass
			else:
				edges = getEdges(graph, vertex)
				if len(edges) == 1:
					if getOtherVertex(edges[0], vertex) == -1:
						print("used")
						return getOtherVertex(edges[0], vertex)


		if bestvertex == None:
			maxEdges = 0
			maxEdgeVertex = None
			for vertex in graph.V:
				if vertex.color == -1:
					if len(getEdges(graph, vertex)) >= maxEdges:
						maxEdges = len(getEdges(graph, vertex))
						maxEdgeVertex = vertex
			return maxEdgeVertex

		return bestvertex


		# return random.choice([v for v in graph.V if v.color == -1])


	# `graph` is an instance of a Graph, `player` is an integer (0 or 1).
	# Should return a vertex `v` from graph.V where v.color == player
	def ChooseVertexToRemove(graph, player):
		
		mindifference = -100000000000
		bestvertex = None
		
		vertices = []
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

				vertices.append(opponentvertices - allyvertices)
			# 	if (opponentvertices - allyvertices) >= maxdifference:
			# 		maxdifference = opponentvertices - allyvertices
			# 		bestvertex = vertex
			# else:
			# 	edges = getEdges(graph, vertex)
			# 	if len(edges) == 1:
			# 		if getOtherVertex(edges[0], vertex).color == -1:
			# 			print("used")
			# 			return getOtherVertex(edges[0], vertex)

		

		vertices.sort()
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
				else:
					edges = getEdges(graph, vertex)
					if len(edges) == 1:
						if getOtherVertex(edges[0], vertex).color == -1:
							print("used")
							return getOtherVertex(edges[0], vertex)
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
				else:
					edges = getEdges(graph, vertex)
					if len(edges) == 1:
						if getOtherVertex(edges[0], vertex).color == -1:
							print("used")
							return getOtherVertex(edges[0], vertex)
			
		return bestvertex


		# Chooses vertex to remove by considering both opposing and ally vertices, but prioritization is unclear
		# mostopponentvertices = 0
		# leastallyvertices = 100000
		# bestvertex = None
		
		# for vertex in graph.V:
		# 	if vertex.color == player:
		# 		opponentvertices = 0
		# 		allyvertices = 0
		# 		for edge in getEdges(graph, vertex):
		# 			if getOtherVertex(edge, vertex).color != player:
		# 				opponentvertices+=1
		# 			else:
		# 				allyvertices+=1
		# 		if opponentvertices >= mostopponentvertices or allyvertices < leastallyvertices:
		# 			mostopponentvertices = opponentvertices
		# 			leastallyvertices = allyvertices
		# 			bestvertex = vertex

		# return bestvertex


		# Chooses vertex to remove by least surrounding ally vertices
		# bestvertex = None
		# mostgoodvertices = 100000

		# for vertex in graph.V:
		# 	if vertex.color == player:
		# 		goodvertices = 0
		# 		for edge in getEdges(graph, vertex):
		# 			if getOtherVertex(edge, vertex).color == player:
		# 				goodvertices+=1
		# 		if goodvertices <= mostgoodvertices:
		# 			mostgoodvertices = goodvertices
		# 			bestvertex = vertex

		# return bestvertex




		# Chooses vertex to remove by most surrounding opponent vertices
		# mostbadvertices = 0
		# bestvertex = None

		# for vertex in graph.V:
		# 	if vertex.color == player:
		# 		badvertices = 0
		# 		for edge in getEdges(graph, vertex):
		# 			if getOtherVertex(edge, vertex).color != player:
		# 				badvertices+=1
		# 		if badvertices >= mostbadvertices:
		# 			mostbadvertices = badvertices
		# 			bestvertex = vertex

		# return bestvertex



# Feel free to put any personal driver code here.
def main():
    pass

if __name__ == "__main__":
    main()