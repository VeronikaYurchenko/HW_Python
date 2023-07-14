# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle
from os import name


def reader_csv(csv_file):
    with open(csv_file, 'r', newline="", encoding='utf-8') as f:
        c_file = csv.reader(f, quoting= csv.QUOTE_ALL)
        lst = []
        for i, (id_, name, access, hash_) in enumerate(c_file):
            if i:
                lst.append({
                    'id': id_,
                    'name': name,
                    'access': access,
                    'hash': hash_
                })
                print(pickle.dumps(lst))


if __name__ == "__main__":
    reader_csv("task_2u.csv")