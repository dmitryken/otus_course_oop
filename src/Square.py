from src.Figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.a = a
        if (type(a) == float or type(a) == int) and (a > 0):
            pass
        else:
            raise ValueError("data are not valid")

    @property
    def perimeter(self):
        return self.a * 4

    def get_area(self):
        return self.a ** 2
