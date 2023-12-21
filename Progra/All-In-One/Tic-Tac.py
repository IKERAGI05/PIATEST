from Game import Game
import random
import sys
import configparser as conf
import numpy as np

class TicTac(Game):
    tab= np.empty((3,3), str)
    def __init__(self):
        config=conf.ConfigParser()
        config.read('conf.ini')
        self.height= int(config.get('TicTac', 'height'))
        self.width= int(config.get('TicTac', 'width'))
        self.tab = np.empty((self.height, self.width), str)

    def game_init(self, config):
        
    def inicializar_tablero(self):
        vacio='-'
        for i in range(0,len(self.tab)):
            for j in range(0,len(self.tab[i])):
              self.tab[i][j]=vacio
    def comprobar_casilla(self ,i, j):
        if self.tab[i-1][j-1]=='X' or self.tab[i-1][j-1]=='O':
            return False
        else:
            return True
    def bienvenida(self):
        print("Bienvenidos al juego de 3 en raya 1v1, disfrutar y que gane el mejor")
        input("Pulsa intro para comenzar")
        self.escoger_turno()
    def escoger_turno(self):
        cont_turnos = 0
        print("Eligiendo quien empieza...")
        self.inicializar_tablero()
        turno=random.choice([True, False])
        if turno:
            print("Comienza el jugador X")
        else:
            print("Comienza el jugador O")
        self.jugar(turno, cont_turnos)
    def pintar_tablero(self ,tab):
        for i in range(0,len(self.tab)):
            for j in range(0,len(self.tab[i])):
                if j==2:
                    print(self.tab[i][j])
                else:
                    print(self.tab[i][j], end=" ")

    def jugar(self, turno, cont):
        cont+=0.5
        condi=True
        self.pintar_tablero(self.tab)
        if self.tablero_lleno() == False:
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
                     if self.comprobar_casilla(x,y):
                         if turno:
                            self.tab[x - 1][y - 1] = "X"
                            if self.comprobar_final('X') == False:
                                 print("Turno del jugador O")
                                 self.jugar(False, cont)
                            else:
                                 self.fin_juego(0, cont)
                         else:
                           self.tab[x - 1][y - 1] = "O"
                           if self.comprobar_final('O') == False:
                                 print("Turno del jugador X")
                                 self.jugar(True, cont)
                           else:
                                 self.fin_juego(1, cont)
                     else:
                          print("Esta casilla esta ocupada")
                          if turno:
                            self.jugar(True)
                          else:
                            self.jugar(False)
                 else:
                    print("introduce un rango valido entre 1 y 3")
                    x = int(input("Escoge la fila\n"))
                    y = int(input("Escoge la columna\n"))
        else:
            self.fin_juego(2, cont)
    def comprobar_final(self, c):
        if (self.tab[0]==[c,c,c]).all() or (self.tab[1]==[c,c,c]).all() or (self.tab[2]==[c,c,c]).all():
            return True
        elif self.tab[0][0]==c and self.tab[1][0]==c and self.tab[2][0]==c:
            return True
        elif self.tab[0][1]==c and self.tab[1][1]==c and self.tab[2][1]==c:
            return True
        elif self.tab[0][2]==c and self.tab[1][2]==c and self.tab[2][2]==c:
            return True
        elif self.tab[0][0]==c and self.tab[1][1]==c and self.tab[2][2]==c:
            return True
        elif self.tab[0][2]==c and self.tab[1][1]==c and self.tab[2][0]==c:
            return True
        else:
            return False
    def tablero_lleno(self):
        for i in range(0, len(self.tab)):
            for j in range(0, len(self.tab[i])):
                if self.tab[i][j]== '-':
                    return False
        return True
    def fin_juego(self, ganador, cont):
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
                self.bienvenida()
                break
            elif vuelta.lower()=="no":
                sys.exit()
                break
            else:
                vuelta = input("Perdona no te he entendido. ¿Quereis repetir?\n")

t= TicTac()

t.bienvenida()