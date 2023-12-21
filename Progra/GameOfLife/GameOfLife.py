import copy
import random
import time
from os import system, name

import numpy as np


class GameOfLife:
    DEFAULT_CELL_WIDTH = 10
    DEFAULT_CELL_HEIGHT = 10
    DEFAULT_INIT_ALIVE_CELLS = 10
    DEFAULT_GAME_TURNS = 10
    DEAD = "."
    ALIVE = "*"

    def __init__(self, width=DEFAULT_CELL_WIDTH, height=DEFAULT_CELL_HEIGHT,
                 init_alive_cells_num=DEFAULT_INIT_ALIVE_CELLS, game_turns=DEFAULT_GAME_TURNS):
        self.width = width
        self.height = height
        self.init_alive_cells_num = init_alive_cells_num
        self.game_turns = game_turns
        self.cells = np.full(shape=(height, width), fill_value=False)


    def init_game(self):
        self.set_init_alive_cells()
        for i in range(self.game_turns):
            print("Turno: ", i)
            self.draw_grid()
            self.next_turn_grid()
            self.__wait()
    def draw_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j]:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()

    def set_init_alive_cells(self):
        my_set = set()
        while len(my_set) < self.init_alive_cells_num:
            fil = random.randint(0, self.height - 1)
            col = random.randint(0, self.width - 1)
            my_set.add((fil, col))
        for elem in my_set:
            self.cells[elem] = True

    def get_cell_living_neighbors(self, y, x):
        cont = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if i < 0 or j < 0 or i >= self.height or j >= self.width or (i == y and j == x):
                    continue
                elif self.cells[i][j]:
                    cont += 1
        return cont

    def next_turn_grid(self):
        new_grid = copy.deepcopy(self.cells)
        for i in range(self.height):
            for j in range(self.width):
                v_vivos = self.get_cell_living_neighbors(i, j)
                if self.cells[i][j]:
                    if v_vivos < 2 or v_vivos > 3:
                        new_grid[i][j] = False
                else:
                    if v_vivos == 3:
                        new_grid[i][j] = True
        self.cells = new_grid

    def __clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def __wait(self):
        time.sleep(1)
