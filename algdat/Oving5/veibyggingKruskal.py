from sys import stdin
from heapq import *

def mst(heap, n):
    #Kruskals
	
	tagged = [0]*n
	edges = 0
	
	forest = []
	
	heaviest = 0
	
	heapify(heap)
	
	while edges < n - 1:
		
		edge = heappop(heap)
		oNode = edge[1]
		dNode = edge[2]

		oTree = -2
		dTree = -3
		
		if tagged[oNode] or tagged[dNode]:
			trees = len(forest)
			for i in range(trees):
				tree = forest[i]
				if oNode in tree:
					oTree = i
				if dNode in tree:
					dTree = i
		
		if dTree == oTree:
			continue
			
		if oTree < -1 and dTree < -1:
			forest.append([oNode,dNode])
		elif oTree > -1 and dTree < -1: 
			forest[oTree].append(dNode)
		elif oTree < -1 and dTree > -1:
			forest[dTree].append(oNode)
		else:
			if oTree > dTree:
				temp = forest.pop(oTree)
				forest[dTree].extend(temp)
			else:
				temp = forest.pop(dTree)
				forest[oTree].extend(temp)
		
		if heaviest < edge[0]:
			heaviest = edge[0]
		
		tagged[oNode] = 1
		tagged[dNode] = 1
		
		edges += 1
		
	return heaviest
	
def read():
	
	linjer = stdin.readlines()
	n = len(linjer)
	node = 0
	heap = []

	for linje in linjer:
		for k in linje.split():
			data = k.split(':')
			edge = (int(data[1]), node , int(data[0]))
			heap.append(edge)

		node += 1
		
	print mst(heap, n)
	
read()