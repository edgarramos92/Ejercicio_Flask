#Snippet Codes for Python
#Video 27: Map, filter, reduce
import numpy as np
def mapping(n):
	return n * n
maped = map(mapping,range(10))
print (list(maped))
#-----------------------------
print (list(filter(lambda a : a > np.mean(list(maped)), list(maped))))

