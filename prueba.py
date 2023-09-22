import json


with open("datos.json", "r") as archivo:
    contenido= json.load(archivo)

for cont in contenido:
    print(cont['nombre'])