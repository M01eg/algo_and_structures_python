'''
 Урок 3
 Задание 6
В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами. Сами
минимальный и максимальный элементы в сумму не включать.
'''

from random import randint

def task6():
    n_arr = randint(5, 10)
    random_array = [randint(-5, 5) for i in range(n_arr)]

    print(f"Сгенерирован массив:\n{random_array}")

    i_min = i_max = 0
    for i, value in enumerate(random_array):
        if value < random_array[i_min]:
            i_min = i
        if value > random_array[i_max]:
            i_max = i

    i_left, i_right = ((i_min, i_max) if i_min < i_max else (i_max, i_min))

    if i_left + 1 == i_right:
        print("Мин. и макс. элементы расположены друг рядом с другом")
    else:
        elsum = 0
        for i in range(i_left + 1, i_right):
            elsum += random_array[i]
        print(f"Сумма эл-тов между мин. и макс. элементами равна: {elsum}")


if __name__ == "__main__":
    task6()
