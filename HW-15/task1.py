# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import os
import os.path
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename="hw-15.log",
                    encoding="utf-8",
                    level=logging.INFO)
logger = logging.getLogger()
Data = namedtuple('Data', ['name', 'extension', 'parent_dir'])


def get_data(path_directory):
    if path_directory == " ":
        path_directory = os.getcwd()
    entries = os.scandir(path_directory)
    datas = []
    for entry in entries:
        name = os.path.splitext(entry.name)[0]
        extension = os.path.splitext(entry.name)[1] if not entry.isdir() else " "
        parent_dir = os.path.basename(os.path.normpath(path_directory))
        datas.append(Data(name, extension, parent_dir))
    logger.info(Data)
    return datas


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-path_directory', metavar='path_directory', type=str, default='')
    args = parser.parse_args()
    print(get_data(args.path_firectory))
