from tkinter import Tk, BOTH, Canvas
from drawing import Point, Line

class Cell():
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, window, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = window
        if self.__win is None:
            return
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)
        if self.has_left_wall:
            self.left_wall = Line(top_left, bottom_left)
            self.left_wall.draw(self.__win, "black")
        if self.has_right_wall:
            self.right_wall = Line(top_right, bottom_right)
            self.right_wall.draw(self.__win, "black")
        if self.has_top_wall:
            self.top_wall = Line(top_left, top_right)
            self.top_wall.draw(self.__win, "black")
        if self.has_bottom_wall:
            self.bottom_wall = Line(bottom_left, bottom_right)
            self.bottom_wall.draw(self.__win, "black")

    def draw_move(self, to_cell, undo = False):
        x_center = (self.__x1 + self.__x2) / 2
        y_center = (self.__y1 + self.__y2) / 2
        to_x_center = (to_cell.__x1 + to_cell.__x2) / 2
        to_y_center = (to_cell.__y1 + to_cell.__y2) / 2
        center = Point(x_center, y_center)
        to_center = Point(to_x_center, to_y_center)
        move_line = Line(center, to_center)
        color = "red"
        if undo:
            color = "gray"
        move_line.draw(self.__win, color)

    def __repr__(self):
        return f"({self.__x1}, {self.__y1}), ({self.__x2}, {self.__y2})"
        