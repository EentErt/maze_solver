from tkinter import Tk, BOTH, Canvas
from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell_1 = Cell(win)
    cell_1.draw(win.canvas, 400, 300, 500, 400)
    win.wait_for_close()


main()