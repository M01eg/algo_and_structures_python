'''
 Урок 3
 Задание 9
Найти максимальный элемент среди минимальных
элементов столбцов матрицы.
'''

from random import randint

MATRIX_M = 5
MATRIX_N = 4

def task9():
    random_matrix = [[randint(0, 9) for j in range(MATRIX_N)] for i in range(MATRIX_M)]

    print(f"Сгенерирована матрица:")
    [print(str(row)) for row in random_matrix]

    min_col_values = []
    for j in range(MATRIX_N):
        min_value = random_matrix[0][j]
        for i in range(MATRIX_M):
            if random_matrix[i][j] < min_value:
                min_value = random_matrix[i][j]
        min_col_values.append(min_value)

    max_from_min_values = min_col_values[0]
    for value in min_col_values:
        if value > max_from_min_values:
            max_from_min_values = value

    print(f"Мин. элементы среди столбцов:\n{min_col_values}")
    print(f"Макс. элемент среди среди мин. эл-тов " +
          f"столбцов матрицы: {max_from_min_values}" )


if __name__ == "__main__":
    task9()
