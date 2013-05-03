list1 = [4,6,1,3]

def merge(data, start, split, end):
	L, R = [], []
	
	for i in range(start,split):
		L.append(data[i])
	for j in range(split, end + 1):
		R.append(data[j])
	
	L.append(4170000000)
	R.append(4170000000)
	
	i,j = 0,0
	for k in range(start,end + 1):
		if L[i] <= R[j]:
			data[k] = L[i]
			i += 1
		else:
			data[k] = R[j]
			j += 1
	return data
	
def mergeSort(data, start, end):
		if 
	return data
	