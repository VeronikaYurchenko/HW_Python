# Напишите функцию для транспонирования матрицы

def matrixTranspose(matrix):
    if not matrix:
        return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]

matrix = [[2, 1, 3], [3, 1, 5], [9, 8, 7]]
print(matrixTranspose(matrix))