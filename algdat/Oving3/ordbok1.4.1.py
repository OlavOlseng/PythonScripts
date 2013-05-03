from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
	entry = Node()
	map['?'] = entry
	for ord in ordliste:
		node = entry
		for i in range(0,len(ord[0])):
			c = ord[0][i]
			if c in node.barn:
				node = node.barn[c]
			else:
				node.barn[c] = Node()
				node = node.barn[c]
				map[ord[0][0:i+1]] = node
		node.posi.append(ord[1])
	return entry


def search(ord, indeks, node):
	if not '?' in ord:
		try:
			return map[ord].posi
		except:
			return []
	else:
		indeks = ord.index('?')
		if indeks == 0:
				return posisjoner(ord, 0, node)
		return posisjoner(ord, indeks, map[ord[0:indeks]])	
	
def posisjoner(ord, indeks, node):	
	if indeks >= len(ord):
		return node.posi
	possie = []
	if ord[indeks] == '?':
		for key in node.barn.keys():
			possie.extend(posisjoner(ord, indeks + 1, node.barn[key]))
	elif ord[indeks] not in node.barn.keys():
		return []	
	else:
		possie.extend(posisjoner(ord, indeks + 1, node.barn[ord[indeks]]))
	return possie
	
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
			print "%s:" % sokeord,
			posi = search(sokeord, 0, toppnode)
			posi.sort()
			for p in posi:
				print p,
			print
	except:
		traceback.print_exc(file=stderr)
map = {}
entry = None
start()
