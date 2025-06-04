from tkinter import Tk, BOTH, Canvas
from window import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell_1 = Cell(win)
    cell_2 = Cell(win)
    cell_1.draw(win.canvas, 400, 300, 500, 400)
    cell_2.draw(win.canvas, 700, 500, 799, 599)
    cell_1.draw_move(cell_2)
    win.wait_for_close()


main()