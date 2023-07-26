# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
from education import Student
from lessons import Lesson

if __name__ == '__main__':
    student_1 = Student('Ivanov', 'Ivan', 'Ivanovich')
    student_2 = Student('Petrov', 'Petr', 'Petrovich')
    student_3 = Student('Viktorova', 'Viktoriya', 'Viktorovna')
    student_4 = Student('Sidorova', 'Mariya', 'Nikolaevna')

    print(student_1)
    print(student_2)
    print(student_3)
    print(student_4)

    # Добавить дисциплины
    student_1.append_to_progress(Lesson('Maths', 2, 10))
    student_1.append_to_progress(Lesson('Physics', 5, 50))
    student_1.append_to_progress(Lesson('Chemistry', 3, 30))

    print(student_1.short_name)
    print(student_1.show_progress())

    # student_2.append_to_progress(Lesson('Chemistry', 4, 30))
    # student_2.append_to_progress(Lesson('Biology', 3, 30))

    print(student_2.short_name)
    print(student_2.show_progress())

    student_1.save_progress()

    # Удалить Иванова
    del student_1

    # Создать Иванова заново - Дисциплины должны подгрузиться из файла
    student_1_1 = Student('Ivanov', 'Ivan', 'Ivanovich')
    print(student_1_1.short_name)
    print(student_1_1.show_progress())