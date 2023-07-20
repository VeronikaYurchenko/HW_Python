# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
from task3 import use_csv, write_to_json


@use_csv('name.csv')
@write_to_json('result.json')
def find_quadratic(*args):
    a, b, c = args
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        return (-b / (2 * a))
    else:
        x1 = (-b + (D) ** 0.5) / (2 * a)
        x2 = (-b - (D) ** 0.5) / (2 * a)
        return (x1, x2)


print(find_quadratic(1, 10, 6))
