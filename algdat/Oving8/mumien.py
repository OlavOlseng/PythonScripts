from sys import stdin, stderr

def getPath(parentGraph, n):
	parent = parentGraph[n]
	route = "%i" % n
	while not parent == 0:
		route = ("%i-" % parent) + route
		parent = parentGraph[parent]
	print "0-" + route
	
def best_path(nm, prob, n):
	vals = [0]*n
	vals[0] = prob[0]
	parents = [None]*n
	parents[0] = 0
	
	for i in range(n-1): 
		cNode = nm[i]
		offer = vals[i]
		for tNode in range(n):
			if cNode[tNode]:
				current = vals[tNode]
				if offer > current:
					parents[tNode] = i
					vals[tNode] = vals[i]*prob[tNode]
	
	return getPath(parents, n-1)
	
def start():	
	n = int(stdin.readline())
	sansynligheter = [float(x) for x in stdin.readline().split()]
	nabomatrise = []
	for linje in stdin:
		naborad = [0] * n
		naboer = [int(nabo) for nabo in linje.split()]
		for nabo in naboer:
			naborad[nabo] = 1
		nabomatrise.append(naborad)
	best_path(nabomatrise, sansynligheter, n)
	
start()
