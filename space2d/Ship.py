from .SpaceObject import SpaceObject
from .Model2d import Model2d
from .Math import multiply_vector_by_matrix

class Ship(SpaceObject):

    rotation_matrix = [
        [1, 0],
        [0, 1]
    ]

    model = None

    def __init__(self):
        super().__init__()
        self.model = Model2d()

    def get_model(self):
        return self.model

    def get_rotated_vertices(self):
        verts = self.model.get_vertices()
        rot = []
        for vert in verts:
            rot.append(multiply_vector_by_matrix(vert, self.rotation_matrix))
        return rot

