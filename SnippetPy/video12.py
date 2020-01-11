#Snippet Codes for Python
#Video 12: Functions
import time
def suma(a,b):
	"""This function sums two numbers"""
	return a + b
a = float(input('Please enter a number: \n'))
b = float(input('Please enter another number: \n'))
print ('%f + %f = %f ' %(a,b,suma(a,b)))
time.sleep(5)
print (help(suma))

