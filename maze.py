from tkinter import Tk, BOTH, Canvas
import random
from cell import Cell
import time


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.seed = random.seed(seed)
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for col in range(self.__num_cols):
            self.__cells.append([])
            for row in range(self.__num_rows):
                cell = Cell(self.__win)
                self.__cells[col].append(cell)
                self.__draw_cell(col, row)
        self.__break_entrance_and_exit()

    def __draw_cell(self, i, j):
        cell_x1 = self.__x1 + (self.__cell_size_x * i)
        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y1 = self.__y1 + (self.__cell_size_y * j)
        cell_y2 = cell_y1 + self.__cell_size_y
        self.__cells[i][j].draw(self.__win, cell_x1, cell_y1, cell_x2, cell_y2)
        self.__animate()

    def __break_entrance_and_exit(self):
        start = self.__cells[0][0]
        end = self.__cells[-1][-1]
        start.has_top_wall = False
        self.__draw_cell(0, 0)
        end.has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
        self.__animate()

    def __break_walls_r(self, i, j):
        cell = self.__cells[i][j]
        cell.visited = True
        while True:
            to_visit = []



    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)


