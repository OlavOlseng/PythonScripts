from sys import stdin
from heapq import *

def mst():
	lines = stdin.readlines()
	n = len(lines)
	
    #Prims
	tagged = [0]*n
	heaviest = 0
	edges = 0
	
	heap = getNode(lines,0)
	heapify(heap)
	tagged[0] = 1
	
	while 1:
		edge = heappop(heap)
		target = edge[1]
		if tagged[target]:
			continue
		
		tagged[target] = 1
		if heaviest < edge[0]:
			heaviest = edge[0]
		
		edges += 1
		if edges == n-1:
			break

		for e in getNode(lines,target):
			if not tagged[e[1]]:
				heappush(heap, e)

	return heaviest

def getNode(nodes, node):
	cNode = []
	line = nodes[node]
	for k in line.split():
		data = k.split(':')
		edge = (int(data[1]), int(data[0]))
		cNode.append(edge)
	return cNode

print mst()