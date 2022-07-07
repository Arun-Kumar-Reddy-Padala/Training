import sys

class Student:
	global dictionary
	dictionary={}
	def __init__(self, regd, name, height):
		self.regd=regd
		self.name=name
		self.height=height
		dictionary[self.regd]=[self.name,self.height]

menu=""
while (menu!=6):
	print("""
=======Menu=======
1. Add Student Height.
2. Modify Student Name.
3. Modify Student Height.
4. Remove Student record.
5. Display the records.
6. Exit.
""")
	try:
		menu=int(input("Enter your choice: "))
		if menu==1:
			student_regd=input("Enter the student registration number: ")
			student_name=input("Enter the student name: ")
			student_height=input("Enter the student height: ")
			student=Student(student_regd,student_name,student_height)
		elif menu==2:
			modify_regd=input("Enter the registration number: ")
			if modify_regd in dictionary:
				modify_name=input("Enter the modified name: ")
				dictionary[modify_regd][0]=modify_name
				print("Name Modified Successfully")
			else:
				print("Please enter a valid Registration Number.")
		elif menu==3:
			modify_regd=input("Enter the registration number: ")
			if modify_regd in dictionary:
				modify_height=input("Enter the modified height: ")
				dictionary[modify_regd][1]=modify_height
				print("Name Modified Successfully")
			else:
				print("Please enter a valid Registration Number.")
		elif menu==4:
			if dictionary=={}:
				print("Cannot Remove from an empty dictioanry.")
			else:
				remove=input("Enter the registration number: ")
				if remove in dictionary:
					dictionary.pop(remove)
					print("Removed Successfully")
				else:
					print("Please enter a valid Registration Number.")
		elif menu==5:
			print(dictionary)
		elif menu==6:
			sys.exit()
	except ValueError:
		print("Please enter a valid number.")
			
