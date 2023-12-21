#EJER 1

edad= int(input("¿Cual es tu edad?\n"))
if edad>=18 :
    print("Eres mayor de edad")
else:
    print("Eres menor")

#EJER 2

contra= "hola123"
contraIntro= input("Introduce tu contraseña\n")

if contra.lower()==contraIntro.lower():
    print("Correcto")
else:
    print("Incorrecto") 