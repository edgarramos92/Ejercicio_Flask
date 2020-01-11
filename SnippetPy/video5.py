#Snippet Codes for Python
#Video 5: Numbers in Python 3

def number(val):
	print (val)
	for i in val:
		if type(i) == int:
			print('%i es un entero'%(i))
		elif type(i) == float:
			print('%f es un flotante'%(i))
		else:
			print('No es un número : %s'%i)
	return 0
val = [1,2/8,3.141582,2.71,100,1e5,-8.9,100000000, 'uno']
number(val)
