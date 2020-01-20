'''
 Урок 3
 Задание 1
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне
от 2 до 9
'''

def task1():
    for dividend in range(2, 100):
        n_multiples = 0
        for divider in range(2, 10):
            if dividend % divider == 0:
                n_multiples += 1
        suffix = 'у' if n_multiples == 1 else 'ам'
        print(f'Число {dividend} кратно {n_multiples} числ{suffix}')


if __name__ == "__main__":
    task1()
