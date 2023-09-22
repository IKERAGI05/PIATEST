import math


    
def elegirAccion():
        accion= int(input("¿Cual eliges?"))

        match accion:
            case 0:
                #salir
                pass
            case 1:
                #agregar
                pass
            case 2:
                #Eliminar
                pass
            case 3: 
                #Modificar
                pass
            case 4:
                #Visualizar
                pass
            case _:        
                print("Opción no disponible")
                pintarTeclado()
                
def pintarTeclado():
        print("Bienvenido al CRUD  que accion deseas realizar")
        print("0: Salir")
        print("1: Agregar")
        print("2: Eliminar")
        print("3: Modificar")
        print("4: Visualizar")
        elegirAccion()


pintarTeclado()