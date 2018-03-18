from .System import System
from space2d import Renderer as rend


def draw_system(system):
    player = System.g
    planets = system.get_planets_list()
    for p in planets:
        rend.render_planet(p)

    ships = system.get_ships_list()
    for s in ships:
        rend.render_ship(p)