from space2d.Math import *
from space2d import SystemController
import sdl2_wrapper as draw

def do():
    draw.h_line(5, 200, 5)
    draw.circle(320, 200, 50)
    draw.filled_triangle(100, 5, 50, 40, 150 ,40)
    draw.flush_screen()
    # SystemController.control()