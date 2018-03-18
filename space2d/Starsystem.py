from .ObjectWithModel import ObjectWithModel
from .Planet import Planet
from .Player import Player
from .Ship import Ship


class Starsystem:
    planets = []
    ships = []
    player = None

    def __init__(self):
        self.planets.append(Planet(0, 0))
        self.ships.append(Ship(0, - self.planets[0].get_radius() - 25))
        self.player = Player(self.ships[0])

    def get_planets_list(self):
        return self.planets

    def get_ships_list(self):
        return self.ships

    def get_player(self):
        return self.player
