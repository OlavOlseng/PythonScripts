	
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
