from .SpaceObject import SpaceObject

class Planet(SpaceObject):
    radius = 1000.0 # i dunno in which measurement units it is lol
    color = None

    def get_radius(self):
        return self.radius