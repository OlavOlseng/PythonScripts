from sys import stdin,stderr
import traceback

def subgraftetthet(matrix, n, entry):
	visited = [0]*n
	connects = [entry]
	nodes = 0
	edges = 0
	
	while connects:
		node = connects.pop()
		index = n*node
		visited[node] = 1
		for i in range(0,n):
			contender = int(matrix[index + i])
			if contender == 1 and visited[i] == 0:
				connects.append(i)
		
	for node in range(0,n):
		index = node*n
		if visited[node]: continue
		nodes += 1
		for conn in range(0,n):
			if node == conn: continue
			if visited[conn] == 0 and matrix[index + conn] == 1:
				edges += 1
	
	if nodes == 0:
		return 0.0
	else:
		return float(edges) / float(nodes**2)

try:
	n = int(stdin.readline())
	matrix = [None] * n**2 # rader
	for i in range(0, n):
		linje = stdin.readline()
		for j in range(0, n):
			matrix[i*n +j] = (linje[j] == '1')
	for linje in stdin:
		start = int(linje)
		print "%.3f" % (subgraftetthet(matrix, n, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)