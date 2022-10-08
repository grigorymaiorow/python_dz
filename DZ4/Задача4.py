# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

num = int(input("Введите натуральную степень k: "))


def magit_to_file(num: int):
    if num > 0:
        with open('text.txt', "a") as file:
            num1 = random.randint(0,100) 
            str_1 = f"{num1}*x^{num}"
            for i in reversed(range(2, num)):
                num1 = random.randint(0,100) 
                if num1 != 0:
                    str_1 += f" + {num1}*x^{i}"
            num1 = random.randint(0,100)
            if num1 != 0:
                str_1 += f" + {num1}*x"
            num1 = random.randint(0,100)
            if num1 != 0:
                print(f"{str_1} + {num1} = 0",file = file)
            else:
                print(f"{str_1} = 0", file = file)
magit_to_file(num)
























# import random

# num = int(input("Введите натуральную степень k: "))

# def func (num,name_file):
#     if num != 0 and num > 0:
#           with open (name_file, 'a') as file:
#             for i in reversed(range(1, num + 1)):
#                 el = random.randint(0,100) 
#                 if el == 0:
#                         continue
#                 print(f"{el}*x^{i} {random.choice(['+', '-'])}", file=file, end=" ")
#             else:
#                 print(f"{el} = 0", file=file)

# func(num,'file.txt')






