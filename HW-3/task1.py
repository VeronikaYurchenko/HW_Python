# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

baggage = {"Рома": ("палатка", "спальник", "мангал", "посуда"),\
                    "Костя": ("спальник", "нож", "вода", "уголь"),\
                    "Влад": ("спальник", "чайник", "мясо", "овощи")}

all_baggage = list(baggage.values())
friends_baggage = set(all_baggage[0])
for bags in all_baggage:
    friends_baggage = friends_baggage.intersection(set(bags))
print(f"Вещи, которые взяли три друга{friends_baggage}")

unique_baggage = {}
for name, bags in baggage.items():
    unique_baggage[name] = set(bags).difference(friends_baggage)
print(f"Уникальные вещи,которые взял каждый друг {unique_baggage}")


