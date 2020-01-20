'''
 Урок 3
 Задание 5
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
'''

from random import randint, uniform

def task5():
    n_arr = randint(5, 10)
    random_array = [round(uniform(-30, 30), 2) for i in range(n_arr)]

    print(f"Сгенерирован массив:\n{random_array}")

    max_negative_value_index = -1
    for i, value in enumerate(random_array):
        if value < 0 and (max_negative_value_index == -1 or
                          value > random_array[max_negative_value_index]):
            max_negative_value_index = i

    if max_negative_value_index == -1:
        print("В массиве нет отрицательных элементов")
    else:
        print(f"Максимальный отрицательный элемент массива: {random_array[max_negative_value_index]}")

if __name__ == "__main__":
    task5()
