'''
 Урок 3
 Задание 7
В одномерном массиве целых чисел определить два
наименьших элемента. Они могут быть как равны между
собой (оба являться минимальными), так и различаться.
'''

from random import randint

def task7():
    n_arr = randint(5, 10)
    random_array = [randint(-5, 5) for i in range(n_arr)]

    print(f"Сгенерирован массив:\n{random_array}")

    i_min1, i_min2 = ((0, 1) if random_array[0] < random_array[1] else (1, 0))
    for i, value in enumerate(random_array[2:]):
        if value < random_array[i_min1]:
            i_min1, i_min2 = i+2, i_min1
        elif value < random_array[i_min2]:
            i_min2 = i+2

    print(f"Минимальный эл-т №1: {random_array[i_min1]}")
    print(f"Минимальный эл-т №2: {random_array[i_min2]}")


if __name__ == "__main__":
    task7()
