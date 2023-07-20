# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали.
# Превратите функции в методы класса. Задачи должны решаться через вызов методов экземпляра.
from random import randint as r
from random import uniform as u


class CreateFileNumbers:
    __min = -1000
    __max = 1000

    def __init__(self, count: int, name: str):
        self.count = count
        self.name = name

    def numbers_file(self):
        with open(self.name, 'w', encoding='utf-8') as f:
            for i in range(self.count):
                temp_res = f'{r(self.__min, self.__max)}|{u(self.__min, self.__max)}'
                f.write(f"{temp_res}\n")


class GenFileNames:
    __min = 4
    __max = 8

    def __init__(self, count: int, names: str):
        self.count = count
        self.names = names

    def gen_names(self):
        vowels = "euioa"
        consonants = "qwrtypsdfghjklzxcvbnm"
        with open(self.names, 'w', encoding='utf-8') as f:
            for i in range(self.count):
                name = ""
                for i in range(r(self.__min, self.__max) // 2):
                    name += (vowels[r(0, len(vowels) - 1)])
                    name += (consonants[r(0, len(consonants) - 1)])
                name = name.capitalize()
                f.write(f"{name}\n")


class GenFileMultiplication:

    def __init__(self, file_name_1: str, file_name_2: str, file_name_3):
        self.file_name_1 = file_name_1
        self.file_name_2 = file_name_2
        self.file_name_3 = file_name_3

    def multiplying(self):
        with (
            open(self.file_name_1, 'r', encoding='utf-8') as f1,
            open(self.file_name_2, 'r', encoding='utf-8') as f2,
            open(self.file_name_3, 'w', encoding='utf-8') as f3
        ):
            lenf1 = sum(1 for i in f1)
            lenf2 = sum(1 for i in f2)
            for _ in range(max(lenf1, lenf2)):
                text = f2.readline()
                if text == '':
                    f2.seek(0)
                    text = f2.readline()
                text = text[:-1]
                num = f1.readline()
                if num == '':
                    f1.seek(0)
                    num = f1.readline()
                num = num[:-1]

                num1, num2 = num.split('|')

                res_mult = int(num1) * float(num2)
                if res_mult < 0:
                    f3.write(f'{text.lower()}, {abs(res_mult)} \n')
                else:
                    f3.write(f'{text.upper()}, {round(res_mult)} \n')


test1 = CreateFileNumbers(7, "test.txt")
test1.numbers_file()
print(test1.name)

test2 = GenFileNames(5, "names.txt")
test2.gen_names()
print(test2.names)

test3 = GenFileMultiplication(test1.name, test2.names, 'new_file.txt')
test3.multiplying()