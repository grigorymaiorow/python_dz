#  Напишите программу, которая принимает число N и вывод последовательность N чисел

# Вариант1
# import random  # тоже самое что и (from random import randint)
# def my_random(n):
#     array = []
#     for _ in range(n):
#         array.append(random.randint(0,100))
#     return array
# n = int(input("Введите число n "))
# print(my_random(n))


# Вариант2
# from random import randint
# for _ in range(int(input("Введите число "))):
#     print(randint(0,100), end = ' ')


# Задача2
# Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Введите число n "))
# for i in range(1, n+1):
#     print(i,':', i*3 + 1,' ', end = " ")


# Задача3
# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# str1 = str(input("Введите первую строку: "))
# print(str1)
# str2 = str(input("Введите вторую строку: "))
# print(str2)


