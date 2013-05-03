from sys import stdin
from heapq import *

def mst(nList, n):
    #Prims
	tagged = [0]*n
	heaviest = 0
	edges = 0
	
	heap = nList[0]
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

		for e in nList[target]:
			if not tagged[e[1]]:
				heappush(heap, e)

	return heaviest

def start():
	lines = stdin.readlines()
	n = len(lines)
	nList = [[] for i in range(n)]
	
	for node in xrange(n):
		line = lines[node]
	
		for k in line.split():
			data = k.split(':')
			dest = int(data[0])
			
			if node <= dest:break
			weight = int(data[1]) 		
			nList[node].append((weight,dest))
			nList[dest].append((weight,node))
		
	print mst(nList, n)
	
start()