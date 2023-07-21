# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
from animals import Cat, Dog, Fish


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"dog": Dog, "cat": Cat, "fish": Fish}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("dog", "Druzhok", "Labrador")
    animal_from_fabric.commands = ["голос", "лежать"]
    print(animal_from_fabric)
