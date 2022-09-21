filename="contact_list.txt"
blackname="black_list.txt"
file=open(filename,'a')
print("We are creating the contact list\n")
while(1):
	name=input("Enter the contact name : ")
	contact=input("Enter contact number: ")
	file.write(name),
	file.write(":"),
	file.write(contact),
	file.write("\n")
	ch=input("Do you want to add more (Y or N)?: ")
	if(ch=='n' or ch=='N'):
		break
print("\n\nList created successfully!!!\n")
file.close()
#Reading the file
while(1):
	print("1. See the phone book and black_list ")
	print("2. Update contact by name")
	print("3. Update contact by contact number ")
	print("4. Delete the whole directory ")
	print("5. Add contact ")
	print("6. Search by name ")
	print("7. Seach by contact number ")
	print("8. Delete any contact by name ")
	print("9. Add to black list ")
	print("0. Finish the program")
	n=int(input('Enter your choice in (1-10) :'))
	if n==1:#Reading the phone directory
		print("\n\n#########   Contact List    #############\n\n")
		file=open(filename,'r')
		data=file.readlines()
		for row in data:
			print(row)
		file.close()
		print("\n\n#########   Black List  ###############\n\n")
		try:
			file=open(blackname,'r')
			data=file.readlines()
			for row in data:
				print(row)
		except:
			print('No directory')
		file.close()
	elif n==2:#contact update by name
		contact_name=input("Enter the name you want to change the contact : ")
		contact_to_change=input("Enter his changed contact : ")
		file=open(filename,'r')
		data=file.readlines()
		temp={}
		for line in data:
			extract_data=line.strip("\n")
			raw=extract_data.split(":")
			raw[0].replace(" ","")
			if (raw[0].lower()).find(contact_name.lower())!=-1:
				temp[raw[0]]=contact_to_change
			elif raw[0]==' ':
				break
			else:
				temp[raw[0]]=raw[1]
		file.close()
		file=open(filename,'w')
		for read in temp:
			file.write(read),
			file.write(" : "),
			file.write(temp[read]),
			file.write(" \n ")
		temp.clear()
		file.close()
	elif n==3: #contact update by contact number
		contact_to_change=input("Enter the contact number to change name : ")
		contact_name=input("Enter the name that you want to give: ")
		file=open(filename,'r')
		data=file.readlines()
		temp={}
		for line in data:
			extract_data=line.strip("\n")
			raw=extract_data.split(":")
			raw[1].replace(" ","")
			if raw[1].find(contact_to_change)!=-1:
				temp[contact_name]=contact_to_change
			elif raw[1]==' ':
				break
			else:
				temp[raw[0]]=raw[1]
		file.close()
		file=open(filename,'w')
		for read in temp:
			file.write(read),
			file.write(" : "),
			file.write(temp[read]),
			file.write(" \n ")
		temp.clear()
		file.close()
	elif n==4:#deleting the whole phone directory
		file=open(filename,'r+')
		file.seek(0)
		file.truncate()
		file=open(blackname,'r+')
		file.seek(0)
		file.truncate()
	elif n==5:#Adding another contact
	    file=open(filename,'a')
	    name=input("Enter the contact name : ")
	    contact=input("Enter contact number: ")
	    file.write(name),
	    file.write(":"),
	    file.write(contact),
	    file.write("\n")
	    file.close()
	elif n==6:#Search by name
		i=0
		search=input("Enter the name you want to search : ")
		file=open(filename,'r')
		data=file.readlines()
		for line in data:
			extract_data=line.strip("\n")
			raw=extract_data.split(":")
			raw[0].replace(" ","")
			if (raw[0].lower()).find(search.lower())!=-1:
				print(raw[0], end=" ")
				print(raw[1])
				i=1
			elif raw[0]==' ':
				break
		file.close()
		if i==0:
			print("Contact not found!!!")
	elif n==7:# search by contact number 
		i=0
		search=input("Enter the contact number you want to search : ")
		file=open(filename,'r')
		data=file.readlines()
		for line in data:
			extract_data=line.strip("\n")
			raw=extract_data.split(":")
			raw[1].replace(" ","")
			if raw[1].find(search)!=-1:
				print(raw[0],end=" ")
				print(raw[1])
				i=1
			elif raw[0]==' ':
				break
		file.close()
		if i==0:
			print("Contact not found!!!")
	elif n==8:
		i=0
		contact_name=input("Enter the contact name you want  delete: ")
		file=open(filename,'r')
		data=file.readlines()
		temp={}
		for line in data:
			extract_data=line.strip("\n")
			raw=extract_data.split(":")
			raw[0].replace(" ","")
			raw[1].replace(" ","")
			if (raw[0].lower()).find(contact_name.lower())!=-1:
				i=1
			elif raw[0]==' ':
				break
			else:
				temp[raw[0]]=raw[1]
		file.close()
		file=open(filename,'w')
		for read in temp:
			file.write(read),
			file.write(" : "),
			file.write(temp[read]),
			file.write(" \n ")
		temp.clear()
		file.close()
		if i==0:
			print("Contact not found!!!!")
	elif n==9:
		i=0
		contact_name=input("Enter the contact name for black_list :")
		file=open(filename,'r')
		data=file.readlines()
		for line in data:
			extract_data=line.strip("\n")
			raw=extract_data.split(":")
			raw[0].replace(" ","")
			raw[1].replace(" ","")
			if (raw[0].lower()).find(contact_name.lower())!=-1:
				contact_naam=raw[0]
				contact_number=raw[1]
				i=1
			elif raw[0]==' ':
				break
		file.close()
		if i==1 and contact_name==contact_naam :
			file=open(blackname,'a')
			file.write(contact_name),
			file.write(":"),
			file.write(contact_number),
			file.write(" \n")
			file.close()
		else:
			print("Contact not found!!!!")
	
	else:#if nothing wanted by the user
		break
	print("\n#########################################\nAgain\n\n")