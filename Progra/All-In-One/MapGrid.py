
import random
from colorama import Fore, Style
class MapGrid:
    def __init__(self, ancho, alto):
        self.ancho=ancho
        self.alto=alto
        self.walls= []
        self.player=[0,0]

    def move_valido(self, movimiento):
        if 0<=movimiento[0]<self.alto and 0<=movimiento[1]<self.ancho:
            for elem in self.walls:
                if elem[0] == movimiento[0] and elem[1]== movimiento[1]:
                    return False
            else:
                return True
        else:
            return False
    def is_final(self):
        if self.player[0]==self.alto-1 and self.player[1]==self.ancho-1:
            return False
        return True
    def draw_grid(self):
        k=0
        for i in range(0, self.alto):
            for j in range(0, self.ancho):
               if (k<len(self.walls)) and (self.walls[k][0]==i) and (self.walls[k][1]==j):
                   print(f"{Fore.RED}#{Style.RESET_ALL}", end=" ")
                   k+=1
               elif i==self.player[0] and j==self.player[1]:
                   print(f"{Fore.GREEN}${Style.RESET_ALL}", end=" ")
               elif i==0 and j==0:
                   print(f"{Fore.YELLOW}<{Style.RESET_ALL}", end=" ")
               elif  i==self.alto-1 and j==self.ancho-1:
                   print(f"{Fore.YELLOW}>{Style.RESET_ALL}", end=" ")
               else:
                   print(".", end=" ")
            print()

    def get_walls(self, porcentaje=0.15):
        myset= set()
        paredes = round(self.ancho * self.alto * porcentaje)
        while len(myset)<paredes:
            fila= random.randint(0,self.alto-1)
            columna= random.randint(0,self.ancho-1)
            if fila==0 and columna==0 or fila==self.alto-1 and columna==self.ancho-1:
                continue
            myset.add((fila, columna))
        self.walls=list(myset)
        self.walls.sort()

    def move_player(self, move):
        movimiento=[]
        if(move=='d'):
            movimiento= [self.player[0],self.player[1]+1]
        elif(move=='a'):
            movimiento= [self.player[0],self.player[1]-1]
        elif(move=='w'):
            movimiento=[self.player[0]-1, self.player[1]]
        elif(move=='s'):
            movimiento=[self.player[0]+1, self.player[1]]
        else:
            return

        if self.move_valido(movimiento):
            self.player=movimiento
        else:
            print("El movimiento no es valido")
        self.draw_grid()

