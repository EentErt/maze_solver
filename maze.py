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
        # self.__cells[1][2] means cell in column 1, row 2
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

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(1)

    def __break_walls_r(self, i, j):
        current = self.__cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            directions = []
            if i > 0: # cell is not in left column
                if self.__cells[i-1][j].visited is False:
                    to_visit.append((i-1, j))
                    directions.append("left")
                    


'''
    def __break_walls_r(self, i, j):
        cell = self.__cells[i][j]
        cell.visited = True
        while True:
            to_visit = []
            directions = []
            if i > 0:
                if self.__cells[i-1][j].visited is False:
                    to_visit.append((i-1, j))
                    directions.append("up")
            if i < self.__num_cols - 1:
                if self.__cells[i+1][j].visited is False:
                    to_visit.append((i+1, j))
                    directions.append("down") # down
            if j > 0:
                if self.__cells[i][j-1].visited is False:
                    to_visit.append((i, j-1))
                    directions.append("left") # left
            if j < self.__num_rows - 1:
                if self.__cells[i][j+1].visited is False:
                    to_visit.append((i, j+1))
                    directions.append("right") # right
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return
            direction = random.randrange(0, len(directions))
            match directions[direction]:
                case "up":
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[i-1][j].has_bottom_wall = False
                    self.__draw_cell(i, j)
                    self.__draw_cell(i-1, j)
                    to_visit.remove((i-1, j))
                    print(f"breaking top wall of ({i}, {j}), moving to ({i-1}, {j})")
                    print(f"visiting cell ({i-1}, {j})")
                    self.__break_walls_r(i-1, j)
                case "down":
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[i+1][j].has_top_wall = False
                    self.__draw_cell(i, j)
                    self.__draw_cell(i+1, j)
                    to_visit.remove((i+1, j))
                    print(f"breaking bottom wall of ({i}, {j}), moving to ({i+1}, {j})")
                    print(f"visiting cell ({i+1}, {j})")
                    self.__break_walls_r(i+1, j)
                case "left":
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[i][j-1].has_right_wall = False
                    self.__draw_cell(i, j)
                    self.__draw_cell(i, j-1)
                    to_visit.remove((i, j-1))
                    print(f"breaking left wall of ({i}, {j}), moving to ({i}, {j-1})")
                    print(f"visiting cell ({i}, {j-1})")
                    self.__break_walls_r(i, j-1)
                case "right":
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[i][j+1].has_left_wall = False
                    self.__draw_cell(i, j)
                    self.__draw_cell(i, j+1)
                    to_visit.remove((i, j+1))
                    print(f"breaking right wall of ({i}, {j}), moving to ({i}, {j+1})")
                    print(f"visiting cell ({i}, {j+1})")
                    self.__break_walls_r(i, j+1)
                case _:
                    continue
            if len(to_visit) > 0:
                self.__break_walls_r(to_visit[0][0], to_visit[0][1])

'''







