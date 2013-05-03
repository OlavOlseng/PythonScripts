from sys import stdin

Inf = float(1E300)

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
			sum += lev(strenger[i],strenger[j],a,b)
		temp.append(sum)
	print temp
	return min(temp)
	
	
linjer = []
for linje in stdin:
    linjer.append(linje.strip())
print minste_avstand(linjer)

