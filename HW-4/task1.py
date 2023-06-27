# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def replacement_with_s(*words):
    words = list(words)
    temp = []
    for i in range(len(words)):
        if words[i].endswith('s') and words[i] != 's':
            temp.append(words[i])
            words[i] = None
    for i in range(len(words)):
        if words[i] is not None:
            words[i] += ''.join([i for i in temp])
    return words


print(replacement_with_s('tasks', 'cats', 'name', '2'))