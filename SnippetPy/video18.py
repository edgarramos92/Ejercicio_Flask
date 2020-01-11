#Snippet Codes for Python
#Video 18: Fibonacci Sequence

i = input('Write a int positive number: ')
try:
	i = int(i)
	if i >= 0:
		print('You type a positive integer number, you  type a %i '%(i))
	else:
		print('You must type a positive integer number, you  type a %i '%(i))
except:
	print('You must type a positive integer number, you  type a %i '%(i))
	



