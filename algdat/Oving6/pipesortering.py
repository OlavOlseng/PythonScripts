from sys import stdin

INF = float(1e3000)

def mergesort(data, l, r):
	#print data[l:r]
	if l < r-1:
		m = (l+r)//2
		mergesort(data,l,m)
		mergesort(data,m,r)
		merge(data,l,r,m)
	
def merge(data, l, r, m):
	print 
	print data[l:r]
	n1 = m-l
	n2 = r-m
	print "n1: ", n1
	print "n2: ", n2
	
	L = [0]*(n1 + 1)
	R = [0]*(n2 + 1)
	L[0] = INF
	R[0] = INF
	
	if n1 == n2:
		for i in range(n1):
			L[n1 - i] = data[l + i]
			R[n1 - i] = data[m + i]
	elif n1 > n2:
		for i in range(n2):
			L[n1 - i] = data[l + i]
			R[n2 - i] = data[m + i]
		L[1] = data[l + n2]
	else:
		for i in range(n1):
			L[n1 - i] = data[l + i]
			R[n2 - i] = data[m + i]
		R[1] = data[m + n1]
	
	print "L: " , L
	print "R: " , R
	
	for i in range(r-l):
		if L[-1] < R[-1]:
			data[l + i] = L.pop()
		else:
			data[l + i] = R.pop()
	
	print "sorted: ", data
		
def bounds(data, lower, upper):
	result = [0,0]

	upperV = data[-1]
	for index in range(len(data)-1,-1,-1):
		if data[index] < upper: break
		upperV = data[index]
		
	lowerV = data[0]
	for index in range(len(data)):
		if data[index] > lower: break
		lowerV = data[index]
		
	result[0] = lowerV
	result[1] = upperV
	return result
	
def read():	
	list = []
	for x in stdin.readline().split():
		list.append(int(x))
	mergesort(list,0,len(list))
	#list2 = insertion(list)
	return
	#print list
	for line in stdin:
		word = line.split()
		lower = int(word[0])
		upper = int(word[1])
		result = bounds(list, lower, upper)
		print str(result[0]) + " " + str(result[1])

read()