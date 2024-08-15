import math


# _________________________Классы____________________________________

class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int):
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1 for i in range(self.sides_count)]
        if self.is_valid_color(*color):
            self.__color = list(color)
            self.filled = True
        else:
            self.filled = False
            print('Параметры цвета вне диапазона, фигура не закрашена')

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
            self.__color = [r, g, b]

    def is_valid_sides(self, *sides: int) -> bool:
        valid = False
        if isinstance(all(sides), int) and all(sides) > 0 and len(sides) == self.sides_count:
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
        if self.is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *sides: int):
        super().__init__(color, *sides)
        self.__radius = radius(self.get_sides()[0])

    def get_radius(self) -> float:
        return self.__radius

    def set_sides(self, *new_sides: int):
        super().set_sides(*new_sides)
        self.__radius = radius(self.get_sides()[0])

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides: int):
        if len(sides) == 3 and sides_of_triangle(*sides):
            super().__init__(color, *sides)
            self.__height = height_triangle(*sides)
        elif len(sides) != 3:
            super().__init__(color, *sides)
        else:
            print('Треугольника с такими сторонами не существует')

    def get_hight(self) -> list:
        return self.__height

    def set_sides(self, *new_sides: int):
        if sides_of_triangle(*new_sides):
            super().set_sides(*new_sides)
            self.__height = height_triangle(*new_sides)
        else:
            print('Треугольника с такими сторонами не существует')

    def get_square(self) -> float:
        p = len(self) / 2
        s = math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides: int):
        if len(sides) == 1:
            arguments = [*sides] * self.sides_count
            super().__init__(color, *arguments)
        else:
            super().__init__(color, *sides)

    def set_sides(self, *new_sides: int):
        if len(new_sides) == 1:
            arguments = [*new_sides] * self.sides_count
            super().set_sides(*arguments)

    def get_volume(self) -> int:
        return self.get_sides()[0] ** 3


# ________________Функции____________________

# радиус окружности по длине окружности
def radius(circumference: int) -> float:
    return circumference / (2 * math.pi)


# список высот треугольника
def height_triangle(a: int, b: int, c: int) -> list:
    p = (a + b + c) / 2
    numerator = 2 * math.sqrt(p * (p - a) * (p - b) * (p - c))
    return [numerator / a, numerator / b, numerator / c]


# провереяет, может ли быть из сторон составлен треугольник
def sides_of_triangle(a: int, b: int, c: int) -> bool:
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # Проверка на создание фигур с ненадлежащим кол-вом сторон:
    print()
    print('Проверка на создание фигур с ненадлежащим кол-вом сторон')
    circle2 = Circle((555, 36, 36), 25, 56)
    print(circle2.get_sides())
    print(circle2.filled)  # фигура не закрашена, так как передавался неправильный параметр цвета
    triangle1 = Triangle((200, 100, 150), 15, 36)
    print(triangle1.get_sides())
    cube2 = Cube((100, 100, 200), 15, 36, 100)
    print(cube2.get_sides())

    # Проверка функций фигур:
    print()
    print('Проверка функций фигур')
    circle2.set_color(150, 150, 150)
    circle2.set_sides(10)
    print(circle2.get_color())
    print(circle2.get_sides())
    print(f'Площадь круга с длиной окружности {len(circle2)} равен: {circle2.get_square()}')
    print(f'Радиус круга с длиной окружности {len(circle2)} равен: {circle2.get_radius()}')
    triangle1.set_sides(1, 2, 4)  # на печать выведет сообщение, что такого треугольника не существует
    triangle1.set_sides(3, 4, 5)
    print(f'Площадь треугольника со сторонами {triangle1.get_sides()} равна: {triangle1.get_square()}')
    print(f'Высоты треугольника со сторонами {triangle1.get_sides()} равны: {triangle1.get_hight()}')
    print(f'Периметр треугольника со сторонами {triangle1.get_sides()} равен: {len(triangle1)}')
