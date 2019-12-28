#Snippet Codes for Python
#Video 32: Urllib

import requests

link = "http://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt" #('A Modern Mean Dwarf Stellar Color and Effective Temperature Sequence', Eric Mamajek) Tabla de temperaturas y tipos espectrales de estrellas
f = requests.get(link)
print(f.text)
