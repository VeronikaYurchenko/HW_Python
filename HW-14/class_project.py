# Доработать класс Project
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках. Передавайте необходимые данные из основного кода проекта.
import json
import sys

from class_exceptions import AccessError, LevelError
from class_user import User


class Project:
    PATH = 'users.json'

    @classmethod
    def users_from_json(cls):
        with open(Project.PATH, 'r', encoding='utf-8') as f:
            dict_json = json.load(f)
            users_lst = []
            for level, users in dict_json.items():
                for user_id, name in users.items():
                    user = User(name, user_id, level)
                    users_lst.append(user)
            return Project(users_lst)

    def __init__(self, users_lst=None):
        if users_lst is None:
            self.users_lst = []
        self.users_lst = users_lst
        self.admin = None

    def login(self, other):
        for user in self.users_lst:
            if user == other:
                other.level = user.level
                self.admin = other
                break
        else:
            raise AccessError(other.name, other.u_id)

    def add_user(self, other):
        if other.level < self.admin.level:
            raise LevelError(other.level, self.admin.level)
        self.users_lst.append(other)

    def remove_user(self, other):
        if other not in self.users_lst:
            raise AccessError(other.name, other.u_id)
        elif other.level < self.admin.level:
            raise LevelError(other.level, self.admin.level)
        self.users_lst.remove(other)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.PATH, 'w', encoding='utf-8') as f:
            my_dict = {}
            for user in self.users_lst:
                if user.level not in my_dict:
                    my_dict[user.level] = {}
                my_dict[user.level][user.user_id] = user.name
            json.dump(my_dict, f)

    def __str__(self):
        return f'Проект {self.__dict__}'

    def run(self):
        print('\n\33[7m' + 'Введите логин для доступа в систему' + '\033[0m\n')
        u = User(input('Ваше имя: '), int(input('Ваш id: ')))
        Project.login(self, 'Успешный вход!')
        print(f'Сейчас вы админ.')
        while True:
            print('\n\33[7m' + 'Главное меню' + '\033[0m\n\n'
                                                '1 - Добавить пользователя\n'
                                                '2 - Удалить пользователяr\n'
                                                '3 - Список пользователей\n'
                                                '4 - Выход\n')
            choice = input('Выберите действие: ')
            match choice:
                case '1':
                    user_1 = User(input("Введите имя пользователя: "), int(input("Введите id пользователя: ")),
                                  int(input("Введите уровень пользователя: ")))
                    Project.add_user(self, user_1)
                    print(f'{user_1} добавлен успешно!')
                case '2':
                    user_2 = User(input("Введите имя пользователя: "), int(input("Введите id пользователя: ")),
                                  int(input("Введите уровень пользователя: ")))
                    Project.remove_user(self, user_2)
                    print(f'{user_2} удален успешно')
                case '3':
                    print('USERS LIST:')
                    for user, number in enumerate(self.users_lst, 1):
                        print('{0}. {1}'.format(user, number))
                case '4':
                    print('\nСписок пользователей сохранен в файл!')
                    print('Хорошего дня!')
                    sys.exit()
                case _:
                    print('Неккоректный ввод! Попробуйте еще раз!')
