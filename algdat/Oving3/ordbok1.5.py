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
		chars = ord[0]
		for i in range(0,len(chars)):
			c = chars[i]
			barn = node.barn
			if c in barn:
				node = barn[c]
			else:
				barn[c] = Node()
				node = barn[c]
				map[chars[0:i+1]] = node
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
	barn = node.barn
	if indeks >= len(ord):
		return node.posi
	possie = []
	c = ord[indeks]
	keys = barn.keys()
	if c == '?':
		for key in keys:
			possie.extend(posisjoner(ord, indeks + 1, barn[key]))
	elif c not in keys:
		return []	
	else:
		possie.extend(posisjoner(ord, indeks + 1, barn[c]))
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
