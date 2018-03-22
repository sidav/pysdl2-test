from space2d.Math import *
from space2d import SystemController
import sdl2_wrapper as draw

def do():
    draw.h_line(5, 200, 5)
    draw.circle(320, 200, 50)
    draw.filled_triangle(100, 5, 40, 40, 150 ,70)
    draw.flush_screen()
    # SystemController.control()