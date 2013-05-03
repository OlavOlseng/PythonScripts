from sys import *
import traceback

def subgraftetthet(matrix, entry):
	n = len(matrix)
	stack = [entry]
	graph = [0]*n
	
	while stack:
		node = stack.pop()
		graph[node] = 1
		for i in range(n):
			if not graph[i] and matrix[node][i]:
				stack.append(i)
				
	subGraph = []
	
	for j in range(n):
		if not graph[j]:
			subGraph.append(j)
	
	edges = 0
	nodes = len(subGraph)
	for node in subGraph:
		for edge in subGraph:
			if matrix[node][edge]:
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
        print "%.3f" % (subgraftetthet(matrix, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)