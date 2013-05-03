from sys import *
import traceback

def subgraftetthet(list, n, entry):
	stack = [entry]
	graph = [0]*n
	
	while stack:
		node = stack.pop()
		graph[node] = 1
		connects = list[node]
		for i in connects:
			if graph[i]:
				continue
			stack.append(i)
			graph[i] = 1 
	
	sub = []
	for i in xrange(n):
		if not graph[i]:
			sub.append(i)
	nodes = len(sub)
	edges = 0
	
	for node in sub:
		for edge in sub:
			if edge in list[node]:
				edges += 1
	if nodes == 0:
		return 0.0
	else:
		return float(edges) / float(nodes**2)

def start():
	try:
		n = int(stdin.readline())
		list = [] * n # rader
		for i in xrange(0, n):
			list[i] = {}
			linje = stdin.readline()
			hash = list[i]
			for j in xrange(0, n):
				if(linje[j] == '1'):
					hash[j] = 1
		for linje in stdin:
			start = int(linje)
			print "%.3f" % (subgraftetthet(list, n, start) + 1E-12)
	except:
		traceback.print_exc(file=stderr)
		
start()