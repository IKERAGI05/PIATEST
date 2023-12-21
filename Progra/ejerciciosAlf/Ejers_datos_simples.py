#EJER 1
print("Hola Mundo")

#EJER 2
str="Hola Mundo"
print(str)

#EJER 3
name=input('¿Cual es tu nombre?\n')

print('Hola ' + name)

#EJER 4
resultado= (((3+2)/(2*5))**2)
print(resultado)

# EJER 5
horas=int(input("¿Cuanto trabajas?\n"))
dinero= int(input("¿Cuanto cobras por hora?\n"))
print(horas*dinero)

#EJER 6
n= int(input("Escribe un número\n"))
a=n*(n+1)/2

print(a)

#EJER 7
peso= float(input("tu peso en kgs\n"))
estatura= float(input("Tu altura en metros\n"))

imc= (peso)/(estatura**2)

print("Tu indice de masa corporal es ", round(imc,2))

#EJER 8
n1= int(input("Primer numero\n"))
m1= int(input("Segundo numero\n"))

cociente= n1/m1
resto= n1%m1

print(n1 , " entre ", m1, " da un cociente ", int(cociente), " y un resto ", resto)

#EJER 9 

inversion= float(input("Cantidad a invertir\n"))
interes= int(input("Interes\n"))
años= int(input("Numero de años\n"))

interesAnual= (interes/100+1)**años
capital= inversion*interesAnual

print("Capital obtenido: ", round(capital, 2))

#EJER 10

pesoP= 112
pesoM= 75

nPayasos= int(input("Numero de payasos\n"))
nMunecas= int(input("Numero de muñecas\n"))

pTotalPayasos= nPayasos*pesoP
pTotalMunecas= nMunecas*pesoM

totalPaquete= pTotalPayasos+pTotalMunecas

print("Peso total del paquete ", totalPaquete, "g")

#EJER 11

interes= 0.04
ingreso= float(input("Deposito\n"))
primerAnyo= ingreso*(interes*1)+ingreso
segundoAnyo= primerAnyo*(interes*1)+primerAnyo
tercerAnyo= segundoAnyo*(interes*1)+segundoAnyo

print("Ahorro el primer año ", round(primerAnyo,2))
print("Ahorro el segundo año ", round(segundoAnyo,2))
print("Ahorro el tercer año ", round(tercerAnyo,2))

#EJER 12

precioPan= 3.49
descuento= (precioPan*60)/100

barrasVendidas=int(input("numero de barras vendidas"))

print("Precio total: ", precioPan*barrasVendidas, "\nPrecio con descuento: ",round((precioPan*barrasVendidas)-descuento,2))