import math
from src.Figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius
        if (type(radius) == float or type(radius) == int) and (radius > 0):
            pass
        else:
            raise ValueError

    @property
    def length(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2
