#CHESSGAME THAT IS MEGA AWESOME

import os

colRef = ['#',' A ',' B ',' C ',' D ',' E ',' F ',' G ',' H ','#']
p1p = ['PWN','TOW','HOR','BIS','KIN','QUE']
p2p = ['pwn','tow','hor','bis','kin','que']


							###BOARD FUNCTIONS###

							
def boardGen():					#GENERATES BOARD
	board = []
	global colRef
	
	#Creates board
	for i in range(10):
		line = []
		for j in range(10):
			line.append('   ')
		board.append(line)
	#Fills edges
	for i in range(10):
		board[i][0] = '%s' % str(i)
		board[i][9] = '%s' % str(i)		
	for i in range(10):
		board[0][i] = colRef[i]
		board[9][i] = colRef[i]

	return board

def boardFill(board):			#FILLS BOARD
	
	#Fills pawns
	for i in range(1,9):
		board[2][i] = 'PWN'
	for i in range(1,9):
		board[7][i] = 'pwn'
	
	#Fills rest
	
	board[1][1] = 'TOW'
	board[1][8] = 'TOW'
	board[8][1] = 'tow'
	board[8][8] = 'tow'
	
	board[1][2] = 'HOR'
	board[1][7] = 'HOR'
	board[8][2] = 'hor'
	board[8][7] = 'hor'
	
	board[1][3] = 'BIS'
	board[1][6] = 'BIS'
	board[8][3] = 'bis'
	board[8][6] = 'bis'
	
	board[1][5] = 'KIN'
	board[1][4] = 'QUE'
	board[8][4] = 'que'
	board[8][5] = 'kin'
	
	return board
'''
def boardFill(board):			#FAKE BOARD TO CHECK FOR CHECKMATE
	board[8][5] = 'kin'
	board[7][1] = 'TOW'
	board[8][1] = 'TOW'
	board[7][8] = 'TOW'
	board[8][8] = 'TOW'
	
	return board
'''
def boardInit():				#CREATES READY2PLAY BOARD
	board = boardFill(boardGen())
	return board
	
def boardPrint(board):			#PRINTS BOARD NICELY TO SCREEN
	os.system("cls")
	for i in range(10):
		print board[i],'\n'

def boardCopy(board): 			#MAKES A TEMPORARY BOARDCOPY
	TB = [] 
	for row in range(0,10):
		temp = []
		for col in range(0,10):
			temp.append(board[row][col])
		TB.append(temp)
	return TB

def pwnToque(board):			#MAKES PWNS TO QUEENS
	for nr in range(1,9):
		if board[1][nr] == 'pwn':
			board[1][nr] = 'que'
		
	for nr in range(1,9):
		if board[8][nr] == 'PWN':
			board[8][nr] = 'QUE'
	
	return board

	
							###MOVING PIECES FUNCTIONS###
		
def check(board,P): 				#CHECKS IF PLAYER IS IN CHECK
	global p1p
	global p2p
	
	
	if P == 1:
		king = 'KIN'
		enemies = p2p
		temP = 2
	else:
		king = 'kin'
		enemies = p1p
		temP = 1
		
	for row in range(1,9):
		for col in range(1,9):
			if board[row][col] in enemies:
				temp = moveTypes(board,row,col,temP)
				if temp == None:
					pass
				else:
					for i in temp:
						if board[int(i[1])][int(i[0])] == king:
							return True
	return False

def checkMate(board,P): 			#CHECKS BOARD FOR CHECK MATE.
	
	for y in range(1,9):
		for x in range(1,9):	
			if pCheck(board,y,x,P) == -1:			
				
				valMoves = moveTypes(board,y,x,P)
				if valMoves == None:
					pass
				else:
					for i in valMoves:
						TB = boardCopy(board)
						TB[int(i[1])][int(i[0])] = TB[y][x]
						TB[y][x] = '   '
						if check(TB,P):
							pass
						else:
							return False
			else:			
				pass
	return True
					
def pCheck(board,rowOut,colOut,P):	#CHECKS WHICH PLAYER A PIECE BELONGS TO
	global p1p
	global p2p
	if P == 1:
		if board[rowOut][colOut] == '   ':
			return 0
		elif board[rowOut][colOut] in p1p:
			return -1
		elif board[rowOut][colOut] in p2p:
			return 1
	else:
		if board[rowOut][colOut] == '   ':
			return 0
		elif board[rowOut][colOut] in p1p:
			return 1
		elif board[rowOut][colOut] in p2p:
			return -1

def towMoves(board,rowIn,colIn,P): 	#CHECKS AND RETURNS VALID MOVES FOR TOWERS
	vDest = []
	
	#CHECKS X MOVES DOWN
	for row in range(rowIn+1,9,1):
		if pCheck(board,row,colIn,P) == 1:
			vDest.append(str(colIn) + str(row))
			break
		elif pCheck(board,row,colIn,P) == -1:
			break
		elif pCheck(board,row,colIn,P) == 0:
			vDest.append(str(colIn) + str(row))

	#CHECKS X MOVES UP
	for row in range(rowIn-1,0,-1):
		if pCheck(board,row,colIn,P) == 1:
			vDest.append(str(colIn) + str(row))
			break
		elif pCheck(board,row,colIn,P) == -1:
			break
		elif pCheck(board,row,colIn,P) == 0:
			vDest.append(str(colIn) + str(row))
	
	#CHECKS Y MOVES LEFT
	for col in range(colIn-1,0,-1):
		if pCheck(board,rowIn,col,P) == 1:
			vDest.append(str(col) + str(rowIn))
			break
		elif pCheck(board,rowIn,col,P) == -1:
			break
		elif pCheck(board,rowIn,col,P) == 0:
			vDest.append(str(col) + str(rowIn))
	
	#CHECKS Y MOVES RIGHT
	for col in range(colIn+1,9,1):
		if pCheck(board,rowIn,col,P) == 1:
			vDest.append(str(col) + str(rowIn))
			break
		elif pCheck(board,rowIn,col,P) == -1:
			break
		elif pCheck(board,rowIn,col,P) == 0:
			vDest.append(str(col) + str(rowIn))
	
	return vDest

def pwnMoves(board,rowIn,colIn,P): 	#CHECKS AND RETURNS VALID MOVES FOR PAWNS
	vDest = []
	
	if P == 1:
		Y = 1
	else:
		Y = -1
	
	#CHECKS FOR DOUBLE/SINGLE MOVES
	if rowIn == 2 and P == 1:
		for row in range(rowIn+Y,rowIn+Y*3,Y):
			if pCheck(board,row,colIn,P) == 0:
				vDest.append(str(colIn) + str(row))
	
	elif rowIn == 7 and P == 2:
		for row in range(rowIn+Y,rowIn+Y*3,Y):
			if pCheck(board,row,colIn,P) == 0:
				vDest.append(str(colIn) + str(row))
	
	else:
		if pCheck(board,rowIn+Y,colIn,P) == 0:
			vDest.append(str(colIn) + str(rowIn+Y))
	
	#CHECKS FOR DIAGONAL ATTACKS
	if pCheck(board,rowIn+Y,colIn+1,P) == 1:
		vDest.append(str(colIn+1) + str(rowIn+Y))
	
	if pCheck(board,rowIn+Y,colIn-1,P) == 1:
		vDest.append(str(colIn-1) + str(rowIn+Y))

	return vDest
	
def bisMoves(board,rowIn,colIn,P): 	#CHECKS AND RETURNS VALID MOVES FOR BISHOPS
	vDest = []
	
	#DOWN/LEFT MOVES
	col = 1
	row = 1
	while rowIn+row <= 8 and colIn-col >= 0:
		if pCheck(board,rowIn+row,colIn-col,P) == 0:
			vDest.append(str(colIn-col) + str(rowIn+row))
		elif pCheck(board,rowIn+row,colIn-col,P) == 1:
			vDest.append(str(colIn-col) + str(rowIn+row))
			break
		elif pCheck(board,rowIn+row,colIn-col,P) == -1:
			break
		col += 1
		row += 1
		
	#DOWN/RIGHT MOVES
	col = 1
	row = 1
	while rowIn+row <= 8 and colIn+col <= 8:
		if pCheck(board,rowIn+row,colIn+col,P) == 0:
			vDest.append(str(colIn+col) + str(rowIn+row))
		elif pCheck(board,rowIn+row,colIn+col,P) == 1:
			vDest.append(str(colIn+col) + str(rowIn+row))
			break
		elif pCheck(board,rowIn+row,colIn+col,P) == -1:
			break
		col += 1
		row += 1
			
	#UP/LEFT MOVES
	col = 1
	row = 1
	while rowIn-row >= 0 and colIn-col >= 0:
		if pCheck(board,rowIn-row,colIn-col,P) == 0:
			vDest.append(str(colIn-col) + str(rowIn-row))
		elif pCheck(board,rowIn-row,colIn-col,P) == 1:
			vDest.append(str(colIn-col) + str(rowIn-row))
			break
		elif pCheck(board,rowIn-row,colIn-col,P) == -1:
			break
		col += 1
		row += 1
	
	#UP/RIGHT MOVES
	col = 1
	row = 1
	while rowIn-row >= 0 and colIn+col <= 8:
		if pCheck(board,rowIn-row,colIn+col,P) == 0:
			vDest.append(str(colIn+col) + str(rowIn-row))
		elif pCheck(board,rowIn-row,colIn+col,P) == 1:
			vDest.append(str(colIn+col) + str(rowIn-row))
			break
		elif pCheck(board,rowIn-row,colIn+col,P) == -1:
			break
		col += 1
		row += 1
		
	return vDest

def horMoves(board,rowIn,colIn,P):	#CHECKS AND RETURNS VALID MOVES FOR KNIGHTS
	vDest = []
	try:
		if pCheck(board,rowIn+2,colIn+1,P) == 1 or pCheck(board,rowIn+2,colIn+1,P) == 0:
			vDest.append(str(colIn+1) + str(rowIn+2))	
	except:
		pass
	try:	
		if pCheck(board,rowIn+2,colIn-1,P) == 1 or pCheck(board,rowIn+2,colIn-1,P) == 0:
			vDest.append(str(colIn-1) + str(rowIn+2))
	except:
		pass
	try:
		if pCheck(board,rowIn-2,colIn+1,P) == 1 or pCheck(board,rowIn-2,colIn+1,P) == 0:
			vDest.append(str(colIn+1) + str(rowIn-2))
	except:
		pass
	try:	
		if pCheck(board,rowIn-2,colIn-1,P) == 1 or pCheck(board,rowIn-2,colIn-1,P) == 0:
			vDest.append(str(colIn-1) + str(rowIn-2))
	except:
		pass
	try:	
		if pCheck(board,rowIn+1,colIn+2,P) == 1 or pCheck(board,rowIn+1,colIn+2,P) == 0:
			vDest.append(str(colIn+2) + str(rowIn+1))
	except:
		pass
	try:	
		if pCheck(board,rowIn-1,colIn+2,P) == 1 or pCheck(board,rowIn-1,colIn+2,P) == 0:
			vDest.append(str(colIn+2) + str(rowIn-1))
	except:
		pass
	try:		
		if pCheck(board,rowIn+1,colIn-2,P) == 1 or pCheck(board,rowIn+1,colIn-2,P) == 0:
			vDest.append(str(colIn-2) + str(rowIn+1))
	except:
		pass
	try:		
		if pCheck(board,rowIn-1,colIn-2,P) == 1 or pCheck(board,rowIn-1,colIn-2,P) == 0:
			vDest.append(str(colIn-2) + str(rowIn-1))
	except:
		pass
	
	return vDest
		
def kinMoves(board,rowIn,colIn,P):	#CHECKS AND RETURNS VALID MOVES FOR KINGS
	vDest = []
	for i in range(3):
		for j in range(3):
			if pCheck(board,rowIn-1+i,colIn-1+j,P) == 0 or pCheck(board,rowIn-1+i,colIn-1+j,P) == 1:
				vDest.append(str(colIn-1+j) + str(rowIn-1+i))
	
	return vDest

def queMoves(board,rowIn,colIn,P):	#CHECKS AND RETURNS VALID MOVES FOR QUEENS
	vDest = []
	
	vDest = towMoves(board,rowIn,colIn,P)
	for i in bisMoves(board,rowIn,colIn,P):
		vDest.append(i)
			
	return vDest
	
def moveTypes(board,rowIn,colIn,P): #CHECKS TYPE, RETURNS VALID MOVES
	if board[rowIn][colIn] == 'tow' or board[rowIn][colIn] == 'TOW':
		return towMoves(board,rowIn,colIn,P)
	
	if board[rowIn][colIn] == 'pwn' or board[rowIn][colIn] == 'PWN':
		return pwnMoves(board,rowIn,colIn,P)
	
	if board[rowIn][colIn] == 'bis' or board[rowIn][colIn] == 'BIS':
		return bisMoves(board,rowIn,colIn,P)
		
	if board[rowIn][colIn] == 'hor' or board[rowIn][colIn] == 'HOR':
		return horMoves(board,rowIn,colIn,P)
	
	if board[rowIn][colIn] == 'kin' or board[rowIn][colIn] == 'KIN':
		return kinMoves(board,rowIn,colIn,P)
		
	if board[rowIn][colIn] == 'que' or board[rowIn][colIn] == 'QUE':
		return queMoves(board,rowIn,colIn,P)

def move(P): 						#CHECKS AND PERFORMS MOVE IF VALID
	
	global colRef
	global board
	
	if check(board,P):
		print 'You are in check, player %s!\n' % P
	moveIn = raw_input('Player %s, make a move:\n' % P).split('-')
	
	try: #MAKES INPUT READEABLE
		colIn = int(colRef.index(' ' + moveIn[0][0] + ' '))
		rowIn = int(moveIn[0][1])
		colOut = int(colRef.index(' ' + moveIn[1][0] + ' '))
		rowOut = int(moveIn[1][1])

	except:
		#os.system("cls")
		boardPrint(board)
		print 'Invalid input, try again...\n'
		return True
	
	if pCheck(board,rowIn,colIn,P) == 1 or pCheck(board,rowIn,colIn,P) == 0 : #CHEKS IF THE PIECE BELONGS TO PLAYING PLAYER
		#os.system("cls")
		boardPrint(board)
		print 'You can only move your own pieces...\n'
		return True
	
	valids = moveTypes(board,rowIn,colIn,P)
	
	if str(colOut)+str(rowOut) in valids:
		
		#MAKES A TEMPORARY BOARDCOPY
		tempBoard = boardCopy(board)
		
		#CHEKCS IF MOVE SETS YOU IN CHECK
		tempBoard[rowOut][colOut] = tempBoard[rowIn][colIn]
		tempBoard[rowIn][colIn] = '   '
		if check(tempBoard,P):
			os.system("cls")
			boardPrint(board)
			print 'This move will leave you in check, try again...\n'
			return True
		
		else:
			board = tempBoard
			return False
		
	else:
		#os.system("cls")
		boardPrint(board)
		print 'Invalid move ...'
		return True
		

							
							###RUNCODE GOES HERE###
										
										
print 'Welcome to super awesome mega chess!\n'

run = True
game = True

while run:
	board = boardInit()
	P=1
	while game:
		board = pwnToque(board)
		if checkMate(board,P):
			game = False
			break
		boardPrint(board)
		turn = True
		while turn:
			turn = move(P)			
		if P == 1:
			P = 2
		else:
			P = 1
	boardPrint(board)
	print 'Player %s has LOST the game!\n' % P
	
	go = raw_input('Would you like to play another game of chess? <yes|no>\n')
	if go == 'yes':
		game = True
	elif go == 'no':
		run = False
		break
	
