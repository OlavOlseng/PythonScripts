from sys import stdin, stderr

def main():
	n,_,_ = [int(i) for i in stdin.readline().split()]
	sources = [int(i) for i in stdin.readline().split()]
	sinks = [int(i) for i in stdin.readline().split()]
	
	if n == 1:
		return 1
	sinkCap = [0]*n
	for sink in sinks:
		sinkCap[sink] = 1
	N = [[]]*n
	for node in xrange(n):
		line = stdin.readline()
		if sinkCap[node]:
			continue
		N[node] = [i for i in xrange(n) if line[2*i]=='1' and i not in sources]
		
	paths = 0
	for s in sources:
		if sinkCap[s]:
			sinkCap[s] = 0
			continue
		parents = [-1]*n
		stack = [s]
		while stack:
			node = stack.pop(0)
			for next in N[node]:
				if parents[next] == -1:
					parents[next] = node
					if not sinkCap[next]:
						stack.append(next)
					else:
						sinkCap[next] = 0
						this = next
						while this != s:
							N[this] = N[parents[this]] + [parents[this]]
							this = parents[this]
						stack = []
						paths += 1
						break
	
	return paths
print main()
		
		