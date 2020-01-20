'''
 Урок 3
 Задание 3
В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
'''

from random import randint

def task3():
    n_arr = randint(5, 10)
    random_array = [randint(-30, 30) for i in range(n_arr)]

    print(f"Сгенерирован массив:\n{random_array}")

    i_min = i_max = 0
    for i, value in enumerate(random_array):
        if value < random_array[i_min]:
            min_i = i
        if value > random_array[i_max]:
            max_i = i

    random_array[i_min], random_array[i_max] = random_array[i_max], random_array[i_min]
    print(f"После замены макс. и мин. чисел получаем:\n{random_array}")


if __name__ == "__main__":
    task3()
