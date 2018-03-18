from .SpaceObject import SpaceObject
from .Model2d import Model2d
from .Math import *

class Ship(SpaceObject):

    rotation_matrix = [
        [1.0, 0.0],
        [0.0, 1.0]
    ]

    model = None

    def __init__(self, x, y):
        super().__init__(x, y)
        self.model = Model2d()

    def get_model(self):
        return self.model

    def get_rotated_vertices(self):
        verts = self.model.get_vertices()
        rot = []
        for vert in verts:
            rot.append(multiply_vector_by_matrix(vert, self.rotation_matrix))
        return rot

    def rotate(self, angle):
        self.rotation_matrix = rotate_matrix(self.rotation_matrix, angle)
        # pass