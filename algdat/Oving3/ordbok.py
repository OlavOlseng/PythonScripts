from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def hashValue(string):
	pass
		
def bygg(ordliste):
	for ord in ordliste:
		if ord[0] not in map:
			map[ord[0]] = []
			map[ord[0]].append(ord[1])
		else:
			map[ord[0]].append(ord[1])

def posisjoner(ord, indeks, node):
	if ord not in map:
		return[]
	return map[ord]
	
def start():
	try:
		ord = stdin.readline().split()
		ordliste = []
		pos = 0
		for o in ord:
			ordliste.append( (o,pos) )
			pos += len(o) + 1
		toppnode = bygg(ordliste)
		for sokeord in stdin:
			sokeord = sokeord.strip()
			print sokeord + ":",
			posi = posisjoner(sokeord, 0, toppnode)
			posi.sort()
			for p in posi:
				print p,
			print
	except:
		traceback.print_exc(file=stderr)


map = {}
start()