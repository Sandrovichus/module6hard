import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int):
        self.__sides = list(sides)
        self.__color = list(color)
        if self.is_valid_color(*color):
            self.filled = True
        else:
            self.filled = False

    def get_color(self) -> list:
        return self.__color

    @staticmethod
    def is_valid_color(r: int, g: int, b: int) -> bool:
        valid = False
        if isinstance(all([r, g, b]), int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            valid = True
        return valid

    def set_color(self, r: int, g: int, b: int):
        if self.is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def is_valid_sides(self, *sides: int) -> bool:
        valid = False
        if isinstance(all(sides), int) and all(sides) > 0 and len(sides) == self.__sides:
            valid = True
        return valid

    def get_sides(self) -> list:
        return self.__sides

    def __len__(self) -> int:
        perimeter = 0
        for i in self.get_sides():
            perimeter += i
        return perimeter

    def set_sides(self, *new_sides: int):
        if self.sides_count == len(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, side: int):
        super().__init__(color, side)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


c = Circle((125, 125, 200), 10)
print(c.sides_count)
print(c.get_sides())
print(c.get_square())
print(c.get_color())
print(c.filled)
print(c.__len__())
c.set_sides(100)   # не меняет радиус. Как можно добиться того, чтобы радиус тоже менялся?
print(c.sides_count)
print(c.get_sides())
print(c.get_square())    
print(c.get_color())
print(c.filled)
print(c.__len__())
