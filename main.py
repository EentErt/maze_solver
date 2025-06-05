from tkinter import Tk, BOTH, Canvas
from window import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 14, 50, 50, win, seed = 1)
    maze.solve()
    win.wait_for_close()



main()