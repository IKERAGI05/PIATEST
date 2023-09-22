import json
class Agregar():
    def __init__(self):
       pass
    
    def agregar(nombreArchivo, persona):
        with open(nombreArchivo, "w") as archivo:
            json.dump(persona, archivo)
    

