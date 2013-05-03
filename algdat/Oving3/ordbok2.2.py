from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
	entry = Node()
	for ord in ordliste:
		chars = ord[0]
		if chars in map:
			map[chars].posi.append(ord[1])
			continue
		node = entry
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
	stack = [node]
	possie = []
	for i in range(indeks, len(ord)):
		c = ord[i]
		temp = []
		while stack:
			node = stack.pop()
			barn = node.barn
			if c == '?':
				temp.extend(barn.values())
			elif c in barn:
				temp.append(barn[c])
		stack = temp
	for i in stack:
		possie.extend(i.posi)
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