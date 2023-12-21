#Ejercicio 10
numeroP= int(input("Introduce un numero: "))
contD=0
for x in range(1,numeroP):
    a=numeroP/x
    if a%2==0:
        contD=contD+1
if contD<2:
    print("Es primo")
else:
    print("no es primo")

#Ejercicio 7
for x in range(1,11):
    for y in range(1,11):
        print(x,"*", y, "= ", x*y)

#Ejercicio 8
n= int(input("Número"))
cadena=''
for x in range(1,n+1,2):
    cadena= str(x) + ' ' + cadena 
    print(cadena)

palabra= input("Escribe una palabra\n")

for i in palabra[::-1]:
   print(i)

frase= input("Escribe una frase\n")
letra= input("letra\n")
cont=0
for i in frase:
    if letra==i:
        cont=cont+1

print(cont)


