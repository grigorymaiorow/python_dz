# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import math
import time

m=32768
a=23
b=12345

def lin_rand_arr_flxd(seed,size):
    if size==1:
        return math.ceil(math.fmod(a*math.ceil(seed)+b,m))
    r=[0 for i in range(size)]
    r[0]=math.ceil(seed)
    for i in range(1,size):
        r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
    return r[1:size]

print(lin_rand_arr_flxd(time.time(),10))


# Var2
# def rnd(prev=None):
#     if prev is None: prev = int(time())
#     rez = (prev * 1103515245 + 12345) % 32767
#     return rez
# 
# # a0 = int(time())
# a1 = rnd()
# a2 = rnd(a1)
# a3 = rnd(a2)

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# my_list = ['4', '5','fdhf', 'hefj']
# num = str(4)
# if num in my_list:
#     print("Зажанное число есть в строке")
# else: print("Заданного числа нет в строке")    


# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# my_str = "qwe"
# count = 0
# req_count = 2
# for i in range(len(my_list)):
#     if my_str == my_list[i]:
#         count += 1
#         if count == req_count:
#             print(f"Позиция i = {i} ")
#             break
# if count <= 1:
#     print("Второго вхождения нет")
