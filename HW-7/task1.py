# 1 — Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

import os
import pathlib



def group_rename(directory, new_name, extension, new_extension):
    files = os.listdir(path=directory)
    count = 1
    for i in files:
        if pathlib.PurePath(i).suffix == new_extension:
            os.rename(f"{directory}\{i}", f"{directory}\{pathlib.PurePath(i).stem}_{new_name}_{count}{extension}")
            count += 1



if __name__ == '__main__':
    directory = "HW-7\task1"
    new_name = 'homework'
    new_extension = '.pdf'
    extension = ".txt"

    group_rename(directory, new_name, extension, new_extension)