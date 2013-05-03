from sys import stdin

def fix(deck, offset):
	n = len(deck)
	sorted = [None]*n
	
	for tup in deck:
		sorted[tup[0] - offset] = tup[1]
	
	ans = ""
	for i in sorted:
		ans += i
	return ans
	
def start():	
	deck = []
	lowest = 2300000000
	
	for line in stdin:
		(letter, list) = line.split(':')
		for i in list.split(','):
			index = int(i)
			if index < lowest:
				lowest = index
			deck.append((int(index),letter))
	print fix(deck, lowest)
	
start()