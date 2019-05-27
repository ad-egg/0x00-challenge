#!/usr/bin/python3
"""MODULE DOCSTRING"""


class Square:
    """a Square class"""

    def __init__(self, *args, **kwargs, width=0, height=0):
        """making a new instance of Square object"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * width

    def perimeter_of_my_square(self):
        """perimeter of square"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """returns width and height of square"""
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
