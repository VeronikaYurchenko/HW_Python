# Напишите следующие функции:
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from functools import wraps


def use_csv(csv_file):
    def deco(func):
        result = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(csv_file, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    args = map(int, row)
                    result.append(func(*args, **kwargs))
            return result
        return wrapper
    return deco


def write_to_json(json_file):
    def deco(func):
        j = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            result = {'args': args,
                       'result': res}
            j.append(result)
            with open(json_file, 'w', encoding='utf-8') as f1:
                json.dump(j, f1, indent=2)
            return result
        return wrapper
    return deco