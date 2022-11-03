class Figure:

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("not geometric figure!!!")
        return self.get_area() + figure.get_area()

    def get_area(self):
        pass
