import os
import shelve

def createdb(db_name):
	try:
		db = shelve.open('budgets/' + db_name + '/data.db', flag = 'n')
		db.close()
		f = open('budgets/' + db_name + '/data.txt', 'w')
		f.close()
	
	except:
		os.system("md budgets\%s" % db_name)
		db = shelve.open('budgets/' + db_name + '/data.db', flag = 'n')
		db.close()
		f = open('budgets/' + db_name + '/data.txt', 'w')
		f.write(str(dbid))
		f.close()
	
	return 0

def transaction(db_name,dbid,date,value,desc):
	db = shelve.open('budgets/' + db_name + '/data.db', flag = 'w', writeback = True)
	db[str(dbid)] = [date,value,desc]
	db.close()
	
	f = open('budgets/' + db_name + '/data.txt', 'w')
	f.write(str(int(dbid)+1))
	f.close()
	return 0

def dbRead(db_name):
	db = shelve.open('budgets/' + db_name + '/data.db', flag = 'r', writeback = False)
	sum = 0
	os.system("cls")
	print 'ID	Date			Description				Value'
	print '------------------------------------------------------------------------------'
	keys = sorted(db)
	keys.sort()
	for i in range(len(keys)):
		lst = db[str(keys[i])]
		s = str(keys[i]).ljust(8) + lst[0].ljust(12) + '\t \t' + lst[2].ljust(24) + str(lst[1]).rjust(22)
		sum = sum + float(lst[1])
		print s
	print '\n \n \t >>> Your balance is: ', str(sum).rjust(9)
	
	db.close()

def dbImport(db_name):
	f = open('budgets/' + db_name + '/data.txt', 'r')
	dbid = int(f.readline())
	os.system("cls")
	
	return dbid
	
def delete(ID,db_name):
	db = shelve.open('budgets/' + db_name + '/data.db', flag = 'w', writeback = True)
	del db[ID]
	
	return ID