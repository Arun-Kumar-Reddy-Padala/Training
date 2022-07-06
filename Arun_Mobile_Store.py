import sys

class Mobile:
	global dictionary
	dictionary={}
	def __init__(self, name, model, units, price):
		self.name=name
		self.model=model
		self.units=units
		self.price=price
		dictionary[self.name]=[self.model,self.units,self.price]
	def display(self):
		return dictionary


choice=""
while choice!=5:
	print("""
=======Menu=======
1. Add a Phone
2. Remove a Phone
3. Display Available Phones
4. Search Available Phone
5. Exit
""")
	try:
		choice=int(input("Enter your choice: "))
		if choice==1:
			name=input("Enter the mobile name along with the model name: ")
			model=input("Enter the mobile make number: ")
			units=int(input("Enter the number of units: "))
			price=int(input("Enter the price of each unit: "))
			mobiles=Mobile(name,model,units,price)
		elif choice==2:
			delete=input("Enter the mobile name along with the model name that you want to remove: ")
			if delete not in dictionary:
				print("Enter a Valid name: ")
			else:
				unit=int(input("Enter the no of units you want to remove: "))
				if unit>dictionary[delete][1]:
					print("Not that many units are available")
				else:
					dictionary[delete][1]-=unit
					print(f"{unit} units removed")
				if dictionary[name][1]==0:
					dictionary.pop(name)
		elif choice==3:
			print(dictionary)
		elif choice==4:
			search=input("Enter the mobile name along with the model name: ")
			print(dictionary[search])
		elif choice==5:
			sys.exit()
	except ValueError:
		print("Please Enter a Valid number")
		
