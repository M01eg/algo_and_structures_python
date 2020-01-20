'''
 Урок 3
 Задание 8
Матрица 5x4 заполняется вводом с клавиатуры кроме
последних элементов строк. Программа должна вычислять
сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести
полученную матрицу.
'''

from random import randint

def task8():
    random_matrix = [[randint(0, 9) if j < 3 else 0 for j in range(4)] for i in range(5)]

    print(f"Сгенерирована матрица:")
    [print(str(row)) for row in random_matrix]

    for row in random_matrix:
        rowsum = 0
        for e in row[:-1]:
            rowsum += e
        row[-1] = rowsum

    print(f"Матрица после вычисления построчных сумм:")
    [print(str(row)) for row in random_matrix]


if __name__ == "__main__":
    task8()
