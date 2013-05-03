from sys import stdin

def fix(deck):
	n = len(deck)
	sorted = [None]*n
	for tup in deck:
		sorted[tup[0] - 1] = tup[1]
	
	ans = ""
	for i in sorted:
		ans += i
	print ans
	
def start():	
	deck = []
	for line in stdin:
		(letter, list) = line.split(':')
		for index in list.split(','):
			deck.append((int(index),letter))
	fix(deck)
	
start()