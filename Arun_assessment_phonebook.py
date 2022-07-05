import sys

menu=""
phonebook={}
while menu!=5:
	print("""
======MENU======
1. Add Contact
2. Delete Contact
3. Display Contacts
4. Search Contact
5. Exit
	""")
	menu=int(input("Enter your option: "))
	if (menu==1):
		temp=[]
		first_name = input("Enter the First Name: ")
		last_name = input("Enter the Last Name: ")
		mobile_number = int(input("Enter the mobile number: "))
		temp.append(first_name)
		temp.append(last_name)
		temp.append(mobile_number)
		phonebook[first_name]=temp
	elif (menu==2):
		delete=input("Enter the contact's first name you want to delete:" )
		if delete in phonebook:
			phonebook.pop(first_name)
			print(f"Contact {delete} is deleted")
		else:
			print("Selected Contact is not in the phonebook.")
	elif (menu==3):
		print(phonebook)

	elif (menu==4):
		search=input("Enter the contact's first name you want to search: ")
		if search in phonebook:
			print(phonebook[search])
		else:
			print("There is no contact named "+search)
	elif (menu==5):
		sys.exit()
