#Snippet Codes for Python
#Video 31: Exceptions

a = input('type a number: ')
try:
	a = int(a)
	print(" %i is an integer number"%a)
except Exception as e:
	print("Error please check: ",e)
	print("Type an integer number!")

