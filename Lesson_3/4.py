'''
 Урок 3
 Задание 4
Определить, какое число в массиве встречается
чаще всего.
'''

from random import randint

def task4():
    n_arr = randint(10, 15)
    random_array = [randint(-5, 5) for i in range(n_arr)]

    print(f"Сгенерирован массив:\n{random_array}")

    number_encounters = dict.fromkeys(random_array, 0)
    for number in random_array:
        number_encounters[number] += 1

    max_values = []
    max_encounter_count = 0
    for value, n_encounters in number_encounters.items():
        if n_encounters > max_encounter_count:
            max_values = [value]
            max_encounter_count = n_encounters
        elif n_encounters == max_encounter_count:
            max_values.append(value)

    print(f"Чаще всего встречаются:\n{', '.join(str(v) for v in max_values)}")


if __name__ == "__main__":
    task4()
