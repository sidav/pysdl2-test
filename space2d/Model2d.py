from .Math import multiply_vector_by_matrix

class Model2d:

    vertices = []
    edges = []

    def __init__(self, vertices=None, edges=None):
        if vertices is None or edges is None:
            self.make_placeholder_model()
        else:
            self.vertices = vertices
            self.edges = edges

    def make_placeholder_model(self):
        self.vertices = [
            [0.0,  -30.0],
            [20.0, -10.0],
            [20.0,  20.0],
            [-20.0, 20.0],
            [-20.0,-10.0],
            [-50.0, 30.0],
            [-30.0, 10.0],
            [50.0,  30.0],
            [30.0,  10.0],
            [0.0,   20.0],
            [10.0,  30.0],
            [-10.0, 30.0]
        ]
        self.edges = [
            [0, 1, 2, 3, 4, 0],
            [7, 8, 2],
            [5, 6, 3],
            [9, 10, 11, 9]
        ]

    def get_edges(self):
        return self.edges

    def get_vertices(self):
        return self.vertices
