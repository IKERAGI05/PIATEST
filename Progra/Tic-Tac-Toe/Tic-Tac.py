import random
import sys

import numpy as np
tab= np.empty((3,3), str)

def inicializar_tablero():
    vacio='-'
    for i in range(0,len(tab)):
        for j in range(0,len(tab[i])):
          tab[i][j]=vacio
def comprobar_casilla(i, j):
    if tab[i-1][j-1]=='X' or tab[i-1][j-1]=='O':
        return False
    else:
        return True
def bienvenida():
    print("Bienvenidos al juego de 3 en raya 1v1, disfrutar y que gane el mejor")
    input("Pulsa intro para comenzar")
    escoger_turno()
def escoger_turno():
    cont_turnos = 0
    print("Eligiendo quien empieza...")
    inicializar_tablero()
    turno=random.choice([True, False])
    if turno:
        print("Comienza el jugador X")
    else:
        print("Comienza el jugador O")
    jugar(turno, cont_turnos)
def pintar_tablero(tab):
    for i in range(0,len(tab)):
        for j in range(0,len(tab[i])):
            if j==2:
                print(tab[i][j])
            else:
                print(tab[i][j], end=" ")

def jugar(turno, cont):
    cont+=0.5
    condi=True
    pintar_tablero(tab)
    if tablero_lleno() == False:
         while True:
                try:
                    x = int(input("Escoge la fila\n"))
                    y = int(input("Escoge la columna\n"))
                    break
                except:
                    print("Introduce SOLO valores númericos")
         while condi:
             if(x>0 and x<4 and y>0 and y<4):
                 condi=False
                 if comprobar_casilla(x,y):
                     if turno:
                        tab[x - 1][y - 1] = "X"
                        if comprobar_final('X') == False:
                             print("Turno del jugador O")
                             jugar(False, cont)
                        else:
                             fin_juego(0, cont)
                     else:
                       tab[x - 1][y - 1] = "O"
                       if comprobar_final('O') == False:
                             print("Turno del jugador X")
                             jugar(True, cont)
                       else:
                             fin_juego(1, cont)
                 else:
                      print("Esta casilla esta ocupada")
                      if turno:
                        jugar(True)
                      else:
                        jugar(False)
             else:
                print("introduce un rango valido entre 1 y 3")
                x = int(input("Escoge la fila\n"))
                y = int(input("Escoge la columna\n"))
    else:
        fin_juego(2, cont)
def comprobar_final(c):
    if (tab[0]==[c,c,c]).all() or (tab[1]==[c,c,c]).all() or (tab[2]==[c,c,c]).all():
        return True
    elif tab[0][0]==c and tab[1][0]==c and tab[2][0]==c:
        return True
    elif tab[0][1]==c and tab[1][1]==c and tab[2][1]==c:
        return True
    elif tab[0][2]==c and tab[1][2]==c and tab[2][2]==c:
        return True
    elif tab[0][0]==c and tab[1][1]==c and tab[2][2]==c:
        return True
    elif tab[0][2]==c and tab[1][1]==c and tab[2][0]==c:
        return True
    else:
        return False
def tablero_lleno():
    for i in range(0, len(tab)):
        for j in range(0, len(tab[i])):
            if tab[i][j]== '-':
                return False
    return True
def fin_juego(ganador, cont):
    cont+=0.5
    if ganador==0:
        print("Felicidades Jugador X has ganado en ", int(cont)," turnos")
    elif ganador==1:
        print("Felicidades Jugador O has ganado en ", int(cont), " turnos")
    else:
        print("Y... esto es un empate, ¿Se merece una revancha?")
    vuelta=input("¿Quereis repetir?\n")

    while True:
        if vuelta.lower()=="si":
            bienvenida()
            break
        elif vuelta.lower()=="no":
            sys.exit()
            break
        else:
            vuelta = input("Perdona no te he entendido. ¿Quereis repetir?\n")

bienvenida()