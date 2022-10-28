import os
os.system('cls||clear')

# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

# def function(n):
#     for i in range(n):
#         print((-3) ** i, end = " ")

# n = int(input("Введите число n: "))
# function(n)


# 12. Длz натурального n создать список, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: [1, 4, 7, 10, 13, 16, 19]

# my_list = []
# n = int(input("Введите число: "))
# for i in range(n +1):
#     my_list.append(i*3 + 1)

# print(my_list)

# Усложнение:
# Создать список, где указанные числа будут стоять на соответствующих индексах, остальные элементы сделать нулевыми, т.е. для индекса 1, значение 1,
# для индекса 4, значение 4 и т.п.
# Пример:
# - Для n = 6: [0,1,0,0,4,0,0,7,0,0,10]

# my_list = []
# n = int(input("Введите число: "))
# for i in range(n + 1):
#     my_list.append(0)
#     my_list.append(i*3 + 1)
#     my_list.append(0)

# my_list.pop()
# print(my_list)

# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

str_scope = '1285564dasd152asdasd12asdasdaswqe1234'                  
str_find = '12'                                                      
                                                                     
find_count = 0                                                       
for i in range(len(str_scope)):                                      
    if str_find == str_scope[i:i+len(str_find)]:                     
        find_count += 1                                              
                                                                     
print(find_count)