# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

base = 16
number = int(input('Введите число: '))
h = hex(number)
print(f'Число:{number}')
print(f'Шестнадцатиричное представление: ' + convert_to(number, base))
print(f'Проверочное: {h}')
