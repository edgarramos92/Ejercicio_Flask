#Snippet Codes for Python
#Video 4: Numbers in Python 2


def number(val):
	if type(val) == int:
		return print('El tipo de número es : '%type(val))
	elif type(val) == long:
		return print('El tipo de número es : '%type(val))
	elif type(val) == float:
		return print('El tipo de número es : '%type(val))
	else:
		return print('No es un número : '%type(val))

val = input('Introduce cualquier número que quieras imprimir: ')
print('Se imprimirá el tipo de número: float, long, int')
number(val)
