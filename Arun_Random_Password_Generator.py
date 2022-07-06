import random

try:
	length=int(input("Enter the length of the password: "))
	if length <0:
		print("Please enter a valid number")
	else:
		password="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*()_+-=/*,./;'\[]<>\?:\" |{}"
		pswd="".join(random.sample(password,length))
		print(pswd)
except ValueError:
	print("Please enter a valid number")


