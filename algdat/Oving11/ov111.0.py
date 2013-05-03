from sys import stdin

def minCoinsGreedy(coins, value):
	iCurrCoin = 0
	iCoins = 0
	while value > 0:
		if coins[iCurrCoin] <= value:
			value -= coins[iCurrCoin]
			iCoins += 1
		else:
			iCurrCoin += 1
	return iCoins
	
'''
def getGreedySet(coins):
	set = [1]
	for c in coins:
		if c == 1:
			continue
		if c%coins[-2] == 0:
			set.append(c)
	set.sort()
	set.reverse()
	return set
'''	
	
def minCoinsDynamic(coins, value):
	if value == 0:
		return 0
	if value in coins:
		return 1
	
	n = len(coins)
	
	goodCoins = []
	for c in coins:
		if c <= value:
			goodCoins.append(c)
			
	results = [INF]*(value+1)
	for i in goodCoins:
		results[i] = 1
	
	for currVal in xrange(1,value+1):
		if results[currVal] != INF:
			continue
		
		min = INF
		for c in goodCoins:
			if c <= currVal:
				current = 1 + results[currVal - c]
				if current < min:
					min = current
		results[currVal] = min
		
	return results
	
def canUseGreedy(coins):
	for i in xrange(len(coins) - 1):
		if coins[i]%coins[i+1] != 0:
			return False
	return True
	
INF = 1000000000
coins = []
for c in stdin.readline().split():
	coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()

if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
	for line in stdin:
		print minCoinsGreedy(coins, int(line))
else:
	values = []
	for line in stdin:
		values.append(int(line))
	results = minCoinsDynamic(coins, max(values))
	for i in values:
		print results[i]
