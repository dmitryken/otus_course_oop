from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, tr_a, tr_b, tr_c):
        self.tr_a = tr_a
        self.tr_b = tr_b
        self.tr_c = tr_c
        if (tr_a + tr_b > tr_c) and (tr_a + tr_c > tr_b) and (tr_b + tr_c > tr_a) \
                and (tr_a > 0) and (tr_b > 0) and (tr_c > 0):
            pass
        else:
            raise ValueError

    @property
    def perimeter(self):
        return self.tr_a + self.tr_b + self.tr_c

    def get_area(self):
        polu_perimetr = (self.tr_a + self.tr_b + self.tr_c) / 2
        return (polu_perimetr * (polu_perimetr - self.tr_a) * (polu_perimetr - self.tr_b) * (
                polu_perimetr - self.tr_c)) ** 0.5
