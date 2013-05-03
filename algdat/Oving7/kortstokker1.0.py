
from sys import stdin
from itertools import repeat

def fix(decks):
	while len(decks) > 2:
		n = len(decks)
		shortest = [(len(decks[0]),0),(len(decks[1]),1)]
		fixShortest(shortest)
			
		for i in range(2,n):
			deck = decks[i]
			if len(deck) < shortest[0][0]:
				shortest[0] = (len(deck), i)
				fixShortest(shortest)
		
		if shortest[0][1] > shortest[1][1]:
			deck1 = decks.pop(shortest[0][1])
			deck2 = decks.pop(shortest[1][1])
		else:
			deck1 = decks.pop(shortest[1][1])
			deck2 = decks.pop(shortest[0][1])
		
		decks.append(merge(deck1,deck2))
		
	done = merge(decks[0],decks[1])
	ans = ""
	for i in done:
		ans+=i[1]
	return ans

def merge(deck1,deck2):
	
	temp = []
	while len(deck1) and len(deck2) > 0:
		if deck1[0][0] < deck2[0][0]:
			temp.append(deck1.pop(0))
		else:
			temp.append(deck2.pop(0))
			
	if len(deck1) == 0:
		while len(deck2) > 0:
			temp.append(deck2.pop(0))
	else:	
		while len(deck1) > 0:
			temp.append(deck1.pop(0))
	
	return temp
	

def fixShortest(shortest):
	if shortest[0][0] < shortest[1][0]:
		temp = shortest[0]
		shortest[0] = shortest[1]
		shortest[1] = temp

def start():
	decks = []
	for line in stdin:
		(index, list) = line.split(':')
		deck = zip(map(int, list.split(',')), repeat(index))
		decks.append(deck)
	return decks 
		
decks = start()
for i in range(1000000):
	print fix(decks)
