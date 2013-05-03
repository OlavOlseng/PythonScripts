#main

import io
import funk
import os
import shelve

u_input = ''
db_name = 'init'
funk.dbNew(db_name)
msg = ''
dbid = 0

print 'Welcome to Budgetty, the console application that lets you track how poor you are!'
raw_input('Press any key to continue...')

while u_input != 'exit':
	
	os.system("cls")
	if msg != '':
		print msg
		raw_input ()
		os.system("cls")
	print 'What would you like to do? (Write help for help)'
	
	u_input = raw_input()
	
	if u_input == 'help':	#SHOWS HELP SCREEN
		os.system("cls")
		funk.help()
		msg = ''
		
	elif u_input == 'budgets': #PRINTS LIST OF BUDGETS
		os.system("cls")
		funk.budgets()
		msg = ''
		raw_input()
		
	elif u_input == 'new':	#CREATES NEW/BLANK BUDGET
		try:
			os.system("cls")
			temp = raw_input('What would you like to name your budget?\n')
			funk.dbNew(temp)
			dbid = 0
			db_name = temp
			msg = 'New budget named %s created...' % db_name
		except:
			msg = 'Error...'
	
	elif u_input == 'delete':	#DELETES ENTRY
		ID = funk.delete(db_name)
		msg = 'Entry %s deleted...' % ID

	elif u_input == 'income' or u_input == 'expense': #PERFORMS TRANSACTIONS
		funk.transaction(db_name,dbid,u_input)
		dbid += 1
		msg = 'Transaction registered.'
	
	elif u_input == 'import': #IMPORTS SHIT
		os.system("cls")
		funk.budgets()
		temp = raw_input('What budget would you like to import?\n')
		dbid = io.dbImport(temp)
		db_name = temp
		msg = 'Budget imported, yeah!'
		
	elif u_input == 'balance': #PRINTS BUDGET AND BALANCE
		funk.balance(db_name)
		msg = ''
		raw_input()
				
	elif u_input == 'exit':	#EXITS BUDGETTY
		os.system("cls")
		break
	
	else:
		msg = 'Invalid input...'
		