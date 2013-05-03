from sys import stdin
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0		

def dfs(rot):
	stack = []
	node = rot
	while not node.ratatosk:
		if(len(node.barn) > 0):	
			for i in node.barn:
				i.nesteBarn += node.nesteBarn + 1
				stack.append(i)
		node = stack.pop()
	return node.nesteBarn
		
def bfs(rot):
	stack = [rot]
	pop = 0
	level = 0
	
	while 1:
		level += 1
		for i in range(pop, len(stack)):
			if stack[pop].ratatosk:
				return level
			stack.extend(stack[pop].barn)
			pop += 1
	return level	

def start():	
	funksjon = stdin.readline().strip()
	antall_noder = int(stdin.readline())
	noder = []
	for i in range(antall_noder):
		noder.append(Node())
	start_node = noder[int(stdin.readline())]
	ratatosk_node = noder[int(stdin.readline())]
	ratatosk_node.ratatosk = True
	for linje in stdin:
		tall = linje.split()
		temp_node = noder[int(tall.pop(0))]
		for barn_nr in tall:
			temp_node.barn.append(noder[int(barn_nr)])
			
		if funksjon == 'dfs':
			print dfs(start_node)
		elif funksjon == 'bfs':
			print bfs(start_node)
		elif funksjon == 'velg':
			# SKRIV DIN KODE HER
			print bfs(start_node)
start()