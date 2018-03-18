from .Starsystem import Starsystem
from space2d import SystemView
from sdl2_wrapper import flush_screen

curr_system = None


def control():
    global curr_system
    curr_system = Starsystem()
    while True:
        SystemView.draw_system(curr_system)
        curr_system.get_player().get_ship().coordy -= 4
        flush_screen()