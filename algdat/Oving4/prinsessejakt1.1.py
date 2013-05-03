from sys import stdin,stderr
import traceback

def subgraftetthet(matrix, n, entry):
	visited = [0]*n
	connects = [entry]
	
	while connects:
		node = connects.pop()
		visited[node] = 1
		for edge in range(0,n):
			contender = matrix[node][edge]
			if contender == 1 and visited[edge] == 0:
				connects.append(edge)
	
	sub = []
	nodes = 0
	for node in range(0,n):
		if not visited[node]:
			sub.append(node)
			nodes += 1
	
	edges = 0
	
	for node in sub:
		for edge in sub:
			if matrix[node][edge] == 1:
				edges += 1
	
	if nodes == 0:
		return 0.0
	else:
		return float(edges) / float(nodes**2)

try:
    n = int(stdin.readline())
    matrix = [None] * n # rader
    for i in range(0, n):
        matrix[i] = [False] * n # kolonner
        linje = stdin.readline()
        for j in range(0, n):
            matrix[i][j] = (linje[j] == '1')
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(matrix, n, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)