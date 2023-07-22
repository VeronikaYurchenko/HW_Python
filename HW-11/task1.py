# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
from time import time, strftime, gmtime


class MyString(str):
    """Расширенный класс строки"""

    def __new__(cls, value, name):
        """Инициализация класса.
        :value: Значение строки.
        :name: Имя автора строки
        """
        instance = super().__new__(cls, value)
        instance.name = name
        instance.init_time = strftime('%H:%M:%S', gmtime(time()))
        return instance

    def __str__(self):
        return str({'value': self} | self.__dict__)


my_line = MyString('What time is it now?', 'Englishman')
print(my_line)