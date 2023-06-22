import fractions
from math import gcd


fraction_1 = input('Введите значение первой дроби в виде "a/b": ')
fraction_2 = input('Введите значение второй дроби в виде "a/b": ')

fract_1a, fract_1b = fraction_1.split('/')
fract_2a, fract_2b = fraction_2.split('/')

if int(fract_1b) == 0 or int(fract_2b) == 0:
    print('Не корректный ввод "ДЕЛЕНИЕ НА НОЛЬ."')
    quit()

# сложение
numerator_add = int(fract_1a) * int(fract_2b) + int(fract_2a) * int(fract_1b)
denominator_add = int(fract_1b) * int(fract_2b)

# произведение
numerator_mult = int(fract_1a) * int(fract_2a)
denominator_mult = int(fract_1b) * int(fract_2b)

# для нахождения нод используем (from math import gcd)
def image(numerator: int, denominator: int) -> str:
    a = gcd(numerator, denominator)
    numerator /= a
    denominator /= a
    numerator = int(numerator)
    denominator = int(denominator)

    if numerator % denominator == 0:
        return f'{int(numerator / denominator)}'
    elif numerator > denominator:
        division = numerator // denominator
        return f'{numerator}/{denominator} = {division} + {numerator - division * denominator}/{denominator}'
    else:
        return f'{numerator}/{denominator}'


print(f'{fraction_1} + {fraction_2} = {image(numerator_add, denominator_add)}')
print(f'{fraction_1} * {fraction_2} = {image(numerator_mult, denominator_mult)}')

# Проверка кода с использованием модуля fractions
print()
print('Проверка')
f1 = fractions.Fraction(int(fract_1a), int(fract_1b))
f2 = fractions.Fraction(int(fract_2a), int(fract_2b))
print(f1 + f2)
print(f1 * f2)
