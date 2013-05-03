import os
import io

def help():
	f = open('help.txt','r')
	text = f.readlines()
	for i in text:
		print i
	f.close()
	raw_input()
		
def budgets():
	os.system("dir budgets")
	
def transaction(db_name,dbid,u_input):
	os.system("cls")
	while 1:
		try:
			date = raw_input('Enter date:\n')
			value = float(input('Enter %s amount:\n' % u_input))
			desc = raw_input('(optional) Enter a short description:\n')
			break
		except:
			os.system("cls")
			print '\n Invalid input...\n'
			
	if u_input == 'expense' and value > 0:
		value = value*-1
	if u_input == 'income' and value < 0:
		value = value*-1
	
	db = io.transaction(db_name,dbid,date,value,desc)
	return db
	
def dbNew(db_name):
	db = io.createdb(db_name)
	return db
	
def balance(db_name):
	io.dbRead(db_name)

def delete(db_name):
	ID = raw_input('What ID would you like to delete?\n')
	io.delete(ID,db_name)
	return ID