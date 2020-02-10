'''
 Урок 8
 Задание 2
Определить количество различных подстрок с использованием
хеш-функции. Задача: на вход функции дана строка, требуется
вернуть количество различных подстрок в этой строке.

Примечание: в сумму не включаем пустую строку и строку целиком.
'''

import hashlib
from collections import Counter

def task2():
    string_to_analyze = input("Введите строку для анализа: ")
    
    all_substrings = [string_to_analyze[i:j]
                      for i in range(len(string_to_analyze))
                      for j in range(i + 1, len(string_to_analyze) + 1)]

    all_substrings.remove(string_to_analyze)  # полную строку не считаем

    substrings_hash_count = Counter()
    for substring in all_substrings:
        substring_hash = hashlib.sha1(substring.encode("utf-8")).hexdigest()
        substrings_hash_count[substring_hash] += 1

    print(f"\nВ строке {len(substrings_hash_count)} уникальных подстрок")

    most_common_hashes = [x[0] for x in substrings_hash_count.most_common(3)]
    most_common_substrings = set()
    for substring in all_substrings:
        substring_hash = hashlib.sha1(substring.encode("utf-8")).hexdigest()
        if substring_hash in most_common_hashes:
            most_common_substrings.add(substring)

    print(f"Топ 3 самых частых подстрок: "
          f'{", ".join(list(most_common_substrings))}')


if __name__ == "__main__":
    task2()
