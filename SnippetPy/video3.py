#Snippet Codes for Python: Este codigo imprimeo "Hello world" al compilarse. 
#Video 3: Introduction to Strings

def printer(val):
	print("Escribió lo siguiente: '%s' "%val)
	print("""Escribió lo siguiente: '%s' """%val)
	print('''Escribió lo siguiente: "%s" '''%val)

	return print('Escribió lo siguiente: "%s" '%val)

val = input('Introduce un valor que quieras imprimir: ')
print('Se imprimirá su oración utilizando distintos signos de comillas')
printer(val)
