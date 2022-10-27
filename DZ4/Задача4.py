# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import os
os.system('cls||clear')
import random

# Вариант1
# num = int(input("Введите натуральную степень k: "))


# def mnogochlen(num: int):
#     if num > 0:
#         str = f""
#         with open("file.txt", "a") as file:
#             for num in range(num,-1,-1):
#                 el = random.randint(0,100)
#                 if el > 0:
#                     if num > 0:
#                         str += f"+{el}*x^{num}"
#                     else:
#                         str += f"+{el}"
#             print(f"{str.replace('+','',1)} = 0", file = file)
# mnogochlen(num)



# Вариант2
# n = int(input("Введите натуральную степень k: "))
n = 4
my_dict = {}

def polinom(n):
    if n > 0:
        for num in range (n, -1,-1):
            el = random.randint(0,100)
            if el > 0:
                if num == 0:
                    my_dict[""] = el
                else:
                    my_dict[f"x^{num}"] = el    
    return my_dict
polinom(n)


def my_string(my_dict):
    str = ""
    for el in my_dict:
        str += f"{my_dict[el]}{el} + "
    str = str[:-2]
    str += "= 0"
    return str
print(my_string(my_dict))


def my_record(my_string):
    with open ("file.txt", 'a') as data:
        data.write(my_string(my_dict))
        data.write("\n")
my_record(my_string)

# Вариант3

# def create_coeffs(num: int) -> list:
#     return [randint(1, 100) for _ in range(num + 1)]


# def create_str(list_coeff: list) -> str:
#     lenght = len(list_coeff)
#     lst_str = [f"{el}*x^{lenght - idx - 1}" for idx, el in enumerate(list_coeff)]
#     return " + ".join(lst_str)


# def write_to_file(polynom_string: str, filename: str) -> None:
#     with open(filename, mode="w", encoding="utf-8") as file:
#         file.write(polynom_string)

# write_to_file(create_str(create_coeffs(10)), "test.txt")

























