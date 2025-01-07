# Генератор файла для задачи тяжелой сложности.

import os
import random

NUMBERS_COUNT = 10_000
MAX_NUMBER = 10_000
REQUIRED_DIVIDER = int('1E', 16)
OUTPUT_FILENAME = '17h.txt'

def convert_to_hex(n):
    result = ''
    while n > 0:
        remainder = n % 16
        if remainder > 9:
            result += chr(ord('A') + remainder - 10)
        else:
            result += str(remainder)
        n //= 16
    return result[::-1]

def gen():
    if os.path.isfile(OUTPUT_FILENAME):
        os.remove(OUTPUT_FILENAME)

    can_divided_count = 0
    with open(OUTPUT_FILENAME, 'a') as f:
        for _ in range(NUMBERS_COUNT):
            while True:
                num1 = round(random.random() * MAX_NUMBER)
                num2 = round(random.random() * MAX_NUMBER)
                if num1 > 0 and num2 > 0:
                    break
            f.write(convert_to_hex(num1) + ' ' + convert_to_hex(num2) + '\n')
            if num1 % REQUIRED_DIVIDER == 0 and num2 % REQUIRED_DIVIDER == 0:
                can_divided_count += 1

    print('В файл', OUTPUT_FILENAME, 'записано', NUMBERS_COUNT, 'строк')
    print('Из них в', can_divided_count, 'строках все числа делятся на 1E')

if __name__ == '__main__':
    gen()