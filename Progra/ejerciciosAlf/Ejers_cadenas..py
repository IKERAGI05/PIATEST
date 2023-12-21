#EJER 1

nombre = input("¿Cómo te llamas?\n")
n = int(input("Introduce un número: "))
print((nombre + "\n") * int(n))

#EJER 2

nombreApel= input("Introduce tu nombre completo\n")
print(nombreApel.upper())
print(nombreApel.lower())
print(nombreApel.title())

#EJER 3

nombre3=input("¿Cual es tu nombre?\n")
print(nombre3.upper(), " tiene", len(nombre3), " letras")

#EJER 4

tlf=input("¿Cual es tu telefono?\n")
print(tlf[4:-3])

#EJER 5

frase= input("Introduce un frase\n")
print(frase[::-1])

#EJER 6

frase2= input("Introduce otra frase\n")
vocal = input("Introduce una vocal\n")
print(frase2.replace(vocal,vocal.upper()))

#EJER 7

correo= input("escribe tu correo \n")
print(correo.replace(correo[(correo.index('@')+1):],'ceu.es'))

#EJER 8

