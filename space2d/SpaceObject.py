
class SpaceObject:
    coordx = coordy = 0.0 # absolute coords in space
    mass = 0.0 # in kilograms lol
    velocity_vector = (0.0, 0.0)

    def get_coords(self):
        return self.coordx, self.coordy