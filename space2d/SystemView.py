from .Starsystem import Starsystem
from space2d import Renderer as rend


def draw_system(system):
    player = system.get_player()
    px, py = player.get_coords()
    print(px, py)
    rend.set_viewpoint(px, py)
    print(rend.viewpoint)

    planets = system.get_planets_list()
    for p in planets:
        rend.render_planet(p)

    ships = system.get_ships_list()
    for s in ships:
        rend.render_object_with_model(s)