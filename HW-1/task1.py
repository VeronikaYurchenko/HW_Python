#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def table() -> iter:
    MIN_LIMIT = 2
    MAX_lIMIT = 10
    COLUMN = 4

    for i in range(MIN_LIMIT, MAX_lIMIT, COLUMN):
        for j in range(MIN_LIMIT, MAX_lIMIT + 1):
            for k in range(i, i + COLUMN):
                if j == MAX_lIMIT and k == i + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='')
                elif k == i + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='')
                else:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='')


table()
