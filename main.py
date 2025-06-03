from window import Window
from drawing import Point, Line

def main():
    win = Window(800, 600)
    point_1 = Point(400, 300)
    point_2 = Point(500, 400)
    line = Line(point_1, point_2)
    win.draw_line(line, "black")
    win.wait_for_close()


main()