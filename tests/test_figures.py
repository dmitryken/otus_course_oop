from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

import pytest
import math

tr_a = 3
tr_b = 4
tr_c = 5

width = 8
height = 5

a = 4

radius = 6


def test_get_area_triangle():
    triangle = Triangle(tr_a, tr_b, tr_c)
    polu_perimeter = (tr_a + tr_b + tr_c) / 2
    assert triangle.get_area() == (polu_perimeter * (polu_perimeter - tr_a) * (polu_perimeter - tr_b)
                                   * (polu_perimeter - tr_c)) ** 0.5


def tests_get_perimeter_triangle():
    triangle = Triangle(tr_a, tr_b, tr_c)
    assert triangle.perimeter == tr_a + tr_b + tr_c


@pytest.mark.parametrize('tr_a, tr_b, tr_c', [('', 4, 5), (3, -1, 5), (3, 4, None)])
def test_create_triangle_wrong_params(tr_a, tr_b, tr_c):
    with pytest.raises(Exception):
        Triangle(tr_a, tr_b, tr_c)


def test_get_area_circle():
    circle = Circle(radius)
    assert circle.get_area() == math.pi * radius ** 2


def test_get_circle_length():
    circle = Circle(radius)
    assert circle.length == 2 * math.pi * radius


@pytest.mark.parametrize('radius', ['', -1, None])
def test_create_circle_wrong_params(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_get_area_rectangle():
    rectangle = Rectangle(width, height)
    assert rectangle.get_area() == width * height


def test_get_perimeter_rectangle():
    rectangle = Rectangle(width, height)
    assert rectangle.perimeter == (width + height) * 2


@pytest.mark.parametrize('width, height', [('', 4), (-1, 5), (3, None)])
def test_create_rectangle_wrong_params(width, height):
    with pytest.raises(Exception):
        Rectangle(width, height)


def test_get_area_square():
    square = Square(a)
    assert square.get_area() == a ** 2


def test_get_perimeter_square():
    square = Square(a)
    assert square.perimeter == a * 4


@pytest.mark.parametrize('side_square', ['', -1, None])
def test_create_square_wrong_params(side_square):
    with pytest.raises(ValueError):
        Square(side_square)


def test_area_triangle_circle_sum():
    triangle = Triangle(tr_a, tr_b, tr_c)
    circle = Circle(radius)
    assert triangle.get_area() + circle.get_area() == triangle.add_area(circle)
