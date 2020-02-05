'''
 Урок 5
 Задание 2
Написать программу сложения и умножения двух
шестнадцатеричных чисел. При этом каждое число
представляется как массив, элементы которого это
цифры числа. Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’,
‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

from collections import defaultdict


class HexNumber:                                     # Я буду складывать и
    def __init__(self, hexstr):                      # умножать эти числа в
        self.num = defaultdict(lambda: "0")          # столбик, поэтому
        for i, character in enumerate(hexstr[::-1]): # сохраняю их в
            self.num[i] = character                  # реверснутом виде
    def __add__(self, other):
        result = HexNumber("0")
        remember_1 = 0
        for i in range(max(len(self.num), len(other.num))):
            digit_add_result = int(self.num[i], 16) + int(other.num[i], 16)
            digit_add_result += remember_1
            result.num[i] = hex(digit_add_result % 16)[2:]
            remember_1 = digit_add_result // 16            # Единичка пойдет
        return result                                      # в следующий разряд
    def __mul__(self, other):
        result = HexNumber("0")
        for i, digit1 in self.num.items():
            for j, digit2 in other.num.items():
                digit_mult_result = int(digit1, 16) * int(digit2, 16)
                result = result + HexNumber(
                    hex(digit_mult_result)[2:] + "0"*(i+j))
        return result
    def __str__(self):
        return ("0x" + "".join(list(self.num.values())[::-1]).lstrip("0"))
        # Побочный эффект использования defaultdict - после
        # сложения чисел иногда появляются лишние нули в левой
        # части числа. Поэтому делаем lstrip("0")


def task2():
    first  = HexNumber(input("Введите первое число в HEX: 0x"))
    second = HexNumber(input("Введите второе число в HEX: 0x"))

    print(f"{str(first)} + {str(second)} = {str(first + second)}")
    print(f"{str(first)} * {str(second)} = {str(first * second)}")


if __name__ == "__main__":
    task2()
