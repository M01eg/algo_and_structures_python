'''
 Урок 8
 Задание 1
Закодируйте любую строку из трех слов
по алгоритму Хаффмана.
'''

from collections import Counter


string_to_encode = "lossless data compression"

char_from_code = Counter(string_to_encode)
code_from_char = {}

def get_char_from_code(code):
    result = list(char_from_code.keys())[0]
    for digit in code:
        result = result[int(digit)]
    return result

def traverse_huffman_tree(code, pair):
    if type(pair[0]) == str:
        code_from_char[pair[0]] = code + '0'
    else:
        traverse_huffman_tree(code + '0', pair[0])
    if type(pair[1]) == str:
        code_from_char[pair[1]] = code + '1'
    else:
        traverse_huffman_tree(code + '1', pair[1])


while len(char_from_code) > 1:
    new_pair = char_from_code.most_common()[-2:]
    del char_from_code[new_pair[0][0]]
    del char_from_code[new_pair[1][0]]
    char_from_code[new_pair[0][0], new_pair[1][0]] = new_pair[0][1] + new_pair[1][1]

traverse_huffman_tree('', list(char_from_code.keys())[0])


def task1():
    encoded_string = [code_from_char[c] for c in string_to_encode]
    print(encoded_string)
    decoded_string = "".join(get_char_from_code(d) for d in encoded_string)
    print(decoded_string)


if __name__ == "__main__":
    task1()
