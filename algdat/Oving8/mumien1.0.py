from sys import stdin, stderr

def getPath(parentGraph, n):
	path = []
	parent = n
	while parent != 0:
		path.append(parent)
		parent = parentGraph[parent]
	path.append(0)
	return '-'.join(map(str, reversed(path)))
	
def best_path(nm, prob, n):
	vals = [0.0]*n
	vals[0] = prob[0]
	parents = [None]*n
	parents[0] = 0
	done = [0]*n
	bNode = 0
	
	for i in range(n-1): 
		cNode = bNode
		bo = -10.0
		done[cNode] = 1
		for tNode in range(n):
			if not done[tNode]:
				if nm[cNode][tNode]:
					offer = vals[cNode]*prob[tNode]
					target = vals[tNode]
					if offer > target:
						parents[tNode] = cNode
						vals[tNode] = offer
				if vals[tNode] > bo:
					bNode = tNode
					bo = vals[tNode]

	if vals[-1] == 0.0:
		return 0
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
	print best_path(nabomatrise, sansynligheter, n)
	
start()
