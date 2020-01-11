#Snippet Codes for Python
#Video 22: List comprehension

with open ("ejemplo20.csv", "r") as myfile:
	ejem = myfile.readlines()

ejem = [x.strip() for x in ejem] 
print (ejem)

