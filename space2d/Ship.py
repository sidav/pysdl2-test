from .SpaceObject import SpaceObject
from .Model2d import Model2d

class Ship(SpaceObject):
    model = None

    def __init__(self):
        super().__init__()
        self.model = Model2d()

    def get_model(self):
        return self.model


