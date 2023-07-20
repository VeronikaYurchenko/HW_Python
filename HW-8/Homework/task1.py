# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle


def transform_pickle(pickle_file, csv_file, csv_write=None):
    with (
        open(pickle_file, 'rb') as f_1,
        open(csv_file, 'w', newline='', encoding='utf-8') as f_2
    ):
        data = pickle.load(f_1)
        csv.write = csv.DictWriter(f_2, fieldnames=data[0], quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)

if __name__ == "__main__":
    transform_pickle("task_2u.pickle", "task_2u.csv")



