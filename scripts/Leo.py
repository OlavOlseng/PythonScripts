#Leonardo tall
import threading

def Leo(n):
	count = 2
	prevev = 1
	prev = 1
	
	if n == 0:
		return 0
	
	while count < n:
		temp = prev + prevev + 1
		prevev = prev
		prev = temp
		count += 1
	return prev

print Leo(5)