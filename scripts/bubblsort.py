#True = False

rawList = [2,1,6,45,76,3,100000,43,1432,0]
sortList = []

i = 1
while i < len(rawList):
	j = 1
	if rawList[i] < rawList[i-j]:
		while j <= i:
			j+=1
			if rawList[i] > rawList[i-j]
				temp = rawList[i-j]
				rawList[i-j] = rawList[i]
				rawList[i] = temp
			i = 1
			continue
	i += 1

print rawList