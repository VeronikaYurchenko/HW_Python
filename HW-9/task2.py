# Напишите следующие функции:
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
import csv
from random import randint as RI


def generation_csv():
    with open('name.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(RI(100, 1000)):
            writer.writerow([RI(-100, 100), RI(-100, 100), RI(-100, 100)])


print(generation_csv())
