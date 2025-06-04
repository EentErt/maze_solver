from tkinter import Tk, BOTH, Canvas
from cell import Cell
import time


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
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
        for row in range(self.__num_rows):
            self.__cells.append([])
            for col in range(self.__num_cols):
                cell = Cell(self.__win)
                self.__cells[row].append(cell)
                self.__draw_cell(row, col)

    def __draw_cell(self, i, j):
        cell_x1 = self.__x1 + (self.__cell_size_x * j)
        cell_x2 = cell_x1 + self.__cell_size_x
        cell_y1 = self.__y1 + (self.__cell_size_y * i)
        cell_y2 = cell_y1 + self.__cell_size_y
        self.__cells[i][j].draw(self.__win, cell_x1, cell_y1, cell_x2, cell_y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)


