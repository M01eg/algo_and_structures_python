'''
 Урок 4
 Задание 1
Проанализировать скорость и сложность одного любого
алгоритма, разработанных в рамках домашнего задания
первых трех уроков.
Примечание: попробуйте написать несколько реализаций
алгоритма и сравнить их.
'''


# Я взял последнюю задачу третьего ДЗ, и адаптировал код для замеров:
###
'''
 Урок 3
 Задание 9
Найти максимальный элемент среди минимальных
элементов столбцов матрицы.
'''
###

from random import random, randint
import timeit

MATRIX_M = 5
MATRIX_N = 4


# Сложность алгоритма генерации O(M*N)
# Генератор можно переписать как два вложенных цикла на M и на N.
# По каждому эл-ту матрицы мы проходим один раз, и кладём в него
# новое только что сгенерированное случайное значение
def generate_random_matrix():
    return [[randint(0, 9) for j in range(MATRIX_N)] for i in range(MATRIX_M)]


# Сложность алгоритма поиска необходимых значений: O(M*N) + O(N)
# 1-ое слагаемое - полностью проходятся все элементы матрицы M*N, и отбираются мин. значения по колонке
# 2-ое слагаемое - в получившемся массиве размером N ищется одно макс. значение
def get_max_from_min_col_values(matrix):
    min_col_values = []
    for j in range(MATRIX_N):
        min_value = matrix[0][j]
        for i in range(MATRIX_M):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
        min_col_values.append(min_value)

    max_from_min_values = min_col_values[0]
    for value in min_col_values:
        if value > max_from_min_values:
            max_from_min_values = value


def task9():
    random_matrix = generate_random_matrix()

    # Не вывожу матрицу, потому что она теперь гораздо больше, чем 5x4:
      #print(f"Сгенерирована матрица:")
      #[print(str(row)) for row in random_matrix]

    n_max = get_max_from_min_col_values(random_matrix)

    #print(f"Мин. элементы среди столбцов:\n{min_col_values}")
    print(f"Макс. элемент среди среди мин. эл-тов " +
          f"столбцов матрицы: {n_max}" )


setup = """
from __main__ import generate_random_matrix, get_max_from_min_col_values, generate_random_matrix_faster
random_matrix = generate_random_matrix()
"""

def measure_performance():
    print("Генерация матрицы длится:")
    print(timeit.timeit("generate_random_matrix()", setup, number=100000))

    print("Поиск нужного значения длится:")
    print(timeit.timeit("get_max_from_min_col_values(random_matrix)", setup, number=100000))


# Оптимизируем генерацию матрицы
# randint слишком медленный, перепишем на стандартный random()
def generate_random_matrix_faster():
    return [[int(random() * 10) for j in range(MATRIX_N)] for i in range(MATRIX_M)]

import cProfile

def measure_performance2():
    print("Оптимизированная генерация матрицы длится:")
    print(timeit.timeit("generate_random_matrix_faster()", setup, number=100000))

    print("Отчет профилировщика - Поиск нужного значения:")
    print(cProfile.runctx(
        "get_max_from_min_col_values(random_matrix)",
        globals(), {"random_matrix": generate_random_matrix()}))


if __name__ == "__main__":
    measure_performance()
    measure_performance2()
