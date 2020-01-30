#### Моя ОС: Windows 7 64-bit, Python 3.8.1 64-bit ####

'''
 Урок 6
 Задание 1
Подсчитать, сколько было выделено памяти под переменные
в ранее разработанных программах в рамках первых трех
уроков. Проанализировать результат и определить программы
с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы
или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность
вашей ОС.
'''

# Моя ОС: Windows 7 64-bit, Python 3.8.1 64-bit

import numpy as np
from urllib.request import urlopen
from memory_profiler import profile


@profile
def task1():
    a = np.random.rand( 500,  1000)
    b = np.random.rand(1000, 30000)

    c = a @ b

    print(c[123][4567])

    f = open("mmul_result_first_row.txt", "w")
    f.write(", ".join(str(round(num, 3)) for num in c[0]))
    f.close()

    print("The cake is a lie!")

    del a
    del b
    del c



@profile
def multiply_random_matrices():
    a = np.random.rand( 500,  1000)
    b = np.random.rand(1000, 30000)

    c = a @ b
    
    return c

@profile
def do_memory_hungry_things():
    n = "Mary had a little lamb".count("a")
    print(f'There are {n} occurrences of the letter "a" in this sentence.')

    c = multiply_random_matrices()
    print("Multiplication successful!")

    try:
        urlopen("https://habr.com/ru/post/000/")
    except:
        print("Oops. Something went wrong!")
        
def procrastinate():
    pass


def task2():
    do_memory_hungry_things()
    print("Job's done. Now let's have some fun.")
    procrastinate()


if __name__ == "__main__":
    task2()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#   Результаты профилирования:
'''
Выполняем:
if __name__ == "__main__":
    task1()

C:\homeworks\6>python task1.py
244.18342345997618
The cake is a lie!
Filename: C:\homeworks\6\task1.py

Line #    Mem usage    Increment   Line Contents
================================================
    21     28.0 MiB     28.0 MiB   @profile                             ##Запускаем профилировщик
    22                             def task1():
    23     31.8 MiB      3.8 MiB       a = np.random.rand( 500,  1000)  ##Выделяем память под первую матрицу
    24    261.2 MiB    229.3 MiB       b = np.random.rand(1000, 30000)  ##Выделяем память под вторую матрицу
    25
    26    378.9 MiB    117.8 MiB       c = a @ b                        ##Память выделяем под результат
    27
    28    378.9 MiB      0.0 MiB       print(c[123][4567])              ##Память под все 3 матрицы продолжает быть выделенной
    29
    30    378.9 MiB      0.0 MiB       f = open("mmul_result_first_row.txt", "w")
    31    381.0 MiB      0.1 MiB       f.write(", ".join(str(round(num, 3)) for num in c[0]))  ##Память под все 3 матрицы продолжает быть выделенной
    32    380.0 MiB      0.0 MiB       f.close()
    33
    34    380.0 MiB      0.0 MiB       print("The cake is a lie!")
    35
    36    376.2 MiB      0.0 MiB       del a                            ##Освобождаем память
    37    146.8 MiB      0.0 MiB       del b                            ##Освобождаем память
    38     32.2 MiB      0.0 MiB       del c                            ##Освобождаем память



'''

#-----------------------------------------------------------------------------------------------------------------------

'''
Выполняем:
if __name__ == "__main__":
    task2()

C:\Python38>python task1.py
There are 4 occurrences of the letter "a" in this sentence.
Filename: C:\homeworks\6\task1.py

Line #    Mem usage    Increment   Line Contents
================================================
    42     27.9 MiB     27.9 MiB   @profile
    43                             def multiply_random_matrices():
    44     31.8 MiB      3.8 MiB       a = np.random.rand( 500,  1000)    #Тоже самое, что и в task1
    45    261.1 MiB    229.3 MiB       b = np.random.rand(1000, 30000)
    46
    47    378.9 MiB    117.8 MiB       c = a @ b
    48
    49    378.9 MiB      0.0 MiB       return c


Multiplication successful!
Oops. Something went wrong!
Filename: C:\homeworks\6\task1.py

Line #    Mem usage    Increment   Line Contents
================================================
    51     27.9 MiB     27.9 MiB   @profile
    52                             def do_memory_hungry_things():
    53     27.9 MiB      0.0 MiB       n = "Mary had a little lamb".count("a")
    54     27.9 MiB      0.0 MiB       print(f'There are {n} occurrences of the letter "a" in this sentence.')
    55
    56    145.7 MiB    117.8 MiB       c = multiply_random_matrices()         #В данном случае память матриц a и b высвобождается
    57    145.7 MiB      0.0 MiB       print("Multiplication successful!")    #после выхода из функции, потому что Питон определяет,
    58                                                                        #что они не имеют ссылок, а матрица c - имеет ссылку
    59    145.7 MiB      0.0 MiB       try:
    60    149.2 MiB      3.4 MiB           urlopen("https://habr.com/ru/post/000/")
    61    149.2 MiB      0.0 MiB       except:
    62    149.2 MiB      0.0 MiB           print("Oops. Something went wrong!")


Job's done. Now let's have some fun.

'''
