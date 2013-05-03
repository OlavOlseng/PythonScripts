from sys import *
import traceback

def subgraftetthet(matrix, n, node):
	# SKRIV DIN KODE HER
	connects = [int(node)]
	visited = [0]*n
	
	while connects:
		node = connects.pop()
		index = n*node
		visited[node] = 1
		for i in range(0,n):
			contender = int(matrix[index + i])
			if contender == 1 and visited[i] == 0:
				connects.append(i)
	
	edges = 0
	verts = 0
	
	for node in range(0,n):
		index = node*n
		if visited[node] == 0:
			verts += 1
			for conn in range(0,n):
				if node == conn: continue
				if visited[conn] == 0 and matrix[index + conn] == '1':
					edges += 1
	
	if verts == 0:
		return 0.0
	else:
		return float(edges) / float(verts**2)


try:
	n = int(stdin.readline())
	matrix = ""
	for i in range(0, n):
		matrix += stdin.readline().strip()	
	for linje in stdin:
		start = int(linje)
		print "%.3f" % (subgraftetthet(matrix, n, start) + 1E-12)
except:
    traceback.print_exc(file=stderr)
