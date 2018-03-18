from .Starsystem import Starsystem
from space2d import SystemView
from sdl2_wrapper import flush_screen

curr_system = None


def control():
    global curr_system
    curr_system = Starsystem()
    SystemView.draw_system(curr_system)
    flush_screen()