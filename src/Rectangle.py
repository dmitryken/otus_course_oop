from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        if (type(width) == float or type(width) == int) and (type(height) == float or type(height) == int) and (
                height > 0) and (width > 0):
            pass
        else:
            raise ValueError

    @property
    def perimeter(self):
        return self.width * 2 + self.height * 2

    def get_area(self):
        return self.width * self.height
