# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.
# --------------------------------------------------------------------------------------------
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.
# ----------------------------------------------------------------------------------------------
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения
class Rectangle:
    """Класс Прямоугольник."""

    def __init__(self, length, width):
        """Инициализация нового экземпляра."""
        self.length = length
        self.width = width if width is not None else length

    def perimeter(self):
        """Расчет периметра прямоугольника."""
        return 2 * (self.length + self.width)

    def area(self):
        """Расчет площади прямоугольника."""
        return self.length * self.width

    def __add__(self, other):
        """Сложение двух прямоугольников."""
        new_perimeter = self.perimeter() + other.perimeter()
        new_length = self.length
        new_width = new_perimeter / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        """Вычитание прямоугольников."""
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_length = min([self.length, self.width, other.length, other.width])
        new_width = new_perimeter / 2 - new_length
        return Rectangle(new_length, new_width)

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        """Сравнение по площади"""
        return self.area() == other.area

    def __str__(self):
        return f'Прямоугольник с длиной: {self.length} и шириной {self.width}'

    def __repr__(self):
        return f'Rectangle ({self.length, self.width})'


rect_1 = Rectangle(2, 5)
print(rect_1)
print(repr(rect_1))

rect_2 = Rectangle(5, 10)
print(rect_2)
print(repr(rect_2))

print (rect_1 == rect_2)

res_sum = rect_1 + rect_2
print(f'{rect_1} + {rect_2} = {res_sum}')

res_sub = rect_1 - rect_2
print(f'{rect_1} - {rect_2} = {res_sub}')