# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

import random

things = {"вода": 5, "овощи": 2.5, "мясо": 3.5, "спальник": 4, "посуда": 1.5, "уголь": 2, "одежда": 3}

backpack = 10
count = 0
List_things = []

while count < backpack:
    key, value = random.choice(list(things.items()))
    if key in List_things:
        continue
    if count + value > backpack:
        break
    count += value
    List_things += (str(key), str(value))
print(List_things, "=", count)
