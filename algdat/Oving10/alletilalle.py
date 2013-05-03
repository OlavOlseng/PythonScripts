from sys import stdin, maxint

def FW_route(aRoute, mNm, iTowns):
	for k in xrange(iTowns):
		for i in xrange(iTowns):
			if k == i: continue
			for j in xrange(iTowns):
				if j == i: continue
				if j == k: continue
				mNm[i][j] = lesser(mNm[i][j],mNm[i][k],mNm[k][j])
	
	sum = mNm[aRoute[-1]][aRoute[0]]
	if sum == -1:
		return "umulig"
	for i in xrange(len(aRoute)-1):
		temp = mNm[aRoute[i]][aRoute[i+1]]
		if temp == -1:
			return "umulig"
		sum += temp
	return sum
	
def lesser(current, first, second):
	if first == -1 or second == -1:
		if current == -1:
			return -1
		return current
	if current == -1:
		return first + second
	return min(current, first + second)
		
tests = int(stdin.readline())

for test in xrange(tests):
	iTowns = int(stdin.readline())
	aRoute = [int(dest) for dest in stdin.readline().split()]
	mNm = [None]*iTowns
	for i in xrange(iTowns):
		mNm[i] = map(int, stdin.readline().strip().split())
	print FW_route(aRoute, mNm, iTowns)