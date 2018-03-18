
class SpaceObject:
    coordx = coordy = 0.0 # absolute coords in space
    mass = 0.0 # in kilograms lol
    velocity_vector = (0.0, 0.0)

    def __init__(self, x, y):
        self.coordx, self.coordy = x, y

    def get_coords(self):
        return self.coordx, self.coordy