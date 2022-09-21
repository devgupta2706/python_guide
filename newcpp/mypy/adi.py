import dbm

db_ms='stud_db'

def create_dbm(data,db_name):
	db = dbm.open(db_name,"c")
	db[data[0]]=",".join("")
	db[data[0]]="".join(data[1])
	db.close()
	
def read_dbm(db_name):
	db=dbm.open(db_name,'r')
	for key, value in db.items():
		print(key, value)
	db.close()
	
def search(db_name,key):
	db=dbm.open(db_name,'r')
	try:
		print(db[key])
	except:
		print('Not found')

def pop_db(db_name,key):
	db=dbm.open(db_name,'c')
	try:
		db.pop(key)
	except:
		print('Not found')
while(1):
	n=int(input("\n\n\n1)Add\n2)Read all db\n3)Search\n4)Pop5)Exit\n"))
	if(n==1):
		name=input("Enter Name: ")
		contact=input("Enter contact no: ")
		create_dbm([name,contact],db_ms)
	elif(n==2):
		read_dbm(db_ms)
	elif(n==3):
		seek=input("\nEnter element for search")
		try:
			search(db_ms,seek)
		except:
			print("Not Found\n")
	elif(n==4):
		seek_to_pop=input("\nEnter name to delete")
		pop_db(db_ms,seek_to_pop)
	else:
		break
		