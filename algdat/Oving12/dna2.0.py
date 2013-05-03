from sys import stdin

Inf = float(1E300)

def lev(s1,s2):
	
	ls1, ls2 = len(s1)+1, len(s2)+1
	m = [None]*(ls1)
	for i in range(ls1):
		m[i] = [0]*(ls2)
		m[i][0] = i
	for j in range(ls2):
		m[0][j] = j
		
	for x in range(1,ls1):
		for y in range(1,ls2):
			rm = m[x-1][y] + 1
			add = m[x][y-1] + 1
			eq = m[x-1][y-1]
			if s1[x-1] != s2[y-1]:
				eq += 1
			m[x][y] = min(rm,add,eq)
			#for i in m: print i
			#print "\n"
	return m[-1][-1]
	
def minste_avstand(strenger):
    # SKRIV DIN KODE HER
	n = len(strenger)
	dists = [0]*n
	for i in range(n-1):
		for j in range(i+1,n):
			sum = lev(strenger[i],strenger[j])
			dists[j] += sum
			dists[i] += sum
	return min(dists)
	
	
linjer = []
for linje in stdin:
    linjer.append(linje.strip())
print minste_avstand(linjer)

#lev(linjer[0],linjer[1])