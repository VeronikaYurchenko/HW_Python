# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def write_json_csv_pickle(path):
    result_dict_json = {}
    for dir_path, dir_file, file_name in os.walk(path):
        result_dict_json[f'DIRECTORY - {dir_path}'] = [
            f'FILE - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
    with open('json_file.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_dict_json, json_file, indent=4, separators=(',', ':'))
    data = [["Dir", "Files"]]
    for key, value in result_dict_json.items():
        data.append([key, value])
    with open('csv_file.csv', 'w', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data)
    # write PICKLE
    with open('pickle_file.bin', 'wb') as pickle_file:
        pickle.dump(result_dict_json, pickle_file)


write_json_csv_pickle(path='directory')