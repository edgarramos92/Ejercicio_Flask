#Snippet Codes for Python
#Video 25: JSON

import json

a = '{"nombre" :"Edgar Ramos", "edad" : 27, "ciudad_origen" : "Guadalajara"}'
b = json.loads(a)
print b["nombre"]

