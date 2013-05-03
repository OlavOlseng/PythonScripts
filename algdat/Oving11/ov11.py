from sys import stdin

def minCoinsGreedy(coins, value):
	iCoins = 0
	iSum = 0
	if value == 0:
		return 0
	while iSum < value:
		for c in coins:
			if c <= value - iSum:
				iSum += c
				iCoins += 1
				break
	return iCoins
	
def minCoinsDynamic(coins, value):
	if value == 0:
		return 0
	if value in coins:
		return 1
	qPoss = [i for i in coins]
	iCoins = 1
	while 1:
		iCoins += 1
		aTemp = []
		while qPoss:
			sum = qPoss.pop()
			for c in coins:
				iTemp = c + sum
				if iTemp == value:
					return iCoins
				if iTemp > value:
					continue
				aTemp.append(iTemp)
		qPoss = aTemp
		
		
	
def canUseGreedy(coins):
	iCoins = len(coins)
	for i in xrange(iCoins - 1):
		if 1.0*coins[i]/coins[i+1] < 2:
			return False
	return True
	
Inf = 1000000000
coins = []
for c in stdin.readline().split():
	coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()

if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
	for line in stdin:
		print minCoinsDynamic(coins, int(line))
else:
	for line in stdin:
		print minCoinsDynamic(coins, int(line))