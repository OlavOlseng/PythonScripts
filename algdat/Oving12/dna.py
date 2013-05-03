from sys import stdin

Inf = float(1E300)
	
def LCS(s1,s2):
	s = ""
	ls1, ls2 = len(s1), len(s2)
	if ls1 == 0 or ls2 == 0:
		return s
	
	if s1[-1] == s2[-1]:
		s = s1[-1] + s
		s1 = s1[0:len(s1)-1]
		s2 = s2[0:len(s2)-1]
		s = LCS(s1,s2) + s
	
	else:
		ls1, ls2 = len(s1), len(s2)
		if ls1 == 0 or ls2 == 0:
			return s
		temp = []
		if len(s1) > 1:
			temp.append(LCS(s1[0:len(s1)-1],s2))
		if len(s2) > 1:
			temp.append(LCS(s1,s2[0:len(s2)-1]))
		max = 0
		ind = -1
		for i in range(len(temp)):
			if len(temp[i]) > max:
				max = len(temp[i])
				ind = i
		if not ind == -1:
			s = temp[ind] + s
	return s

def lev(s1,s2, i, j):
	count = 0
	
	if i == 0:
		return j
	elif j == 0:
		return i
	else:
		count += min(lev(s1,s2,i,j-1) + 1, lev(s1,s2,i-1,j) + 1, lev(s1,s2,i-1,j-1) + (s1[i] != s2[j]))
		return count
		
def minste_avstand(strenger):
    # SKRIV DIN KODE HER
	temp = []
	n = len(strenger)
	for i in range(n):
		sum = 0
		a = len(strenger[i])-1
		for j in range(n):
			if i == j:
				continue
			b = len(strenger[j])-1
			sum +=lev(strenger[i],strenger[j],a,b)
		temp.append(sum)
	return min(temp)
	
	
linjer = []
for linje in stdin:
    linjer.append(linje.strip())
print minste_avstand(linjer)

