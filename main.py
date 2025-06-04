from tkinter import Tk, BOTH, Canvas
from window import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(100, 100, 5, 5, 76, 100, win)
    win.wait_for_close()


main()