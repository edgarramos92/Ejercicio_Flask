#Snippet Codes for Python
#Video 20: CSV

import csv

archivo = open('ejemplo20.csv')
read = csv.reader(archivo)
for i in read:
	print i



