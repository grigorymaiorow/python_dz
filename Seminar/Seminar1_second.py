# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет


# def check(a,b):
#     if a ** 2 == b or b ** 2 == a:
#         print("Да")
#     else:
#         print("Нет")

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# check(a,b)



# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# my_list = []
# for i in range(5):
#     my_list.append(int(input("Введите число: ")))
# print(my_list)

# max = my_list[0]

# for el in my_list:
#     if el > max:
#         max = el
# print(max)



# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input("Введите число: "))
# a  = -n

# for i in range(-n, n+1):
#     print(i, end = ",")

#или

# while a <= n:
#     print(a, end = ",")
#     a += 1


# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# num = float(input("Введите дробное число: "))

# num = 0.1005
# el = int((num)*10)%10
# print(el)

# num = "6,878"
# lst = num.split(",")
# print(lst[1][0])

# num[num.find(",")+1]


# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# num = int(input("Введите число: "))

# if ((num % 5  == 0 and num % 10 == 0) or (num % 15 == 0)) and not num % 30 == 0:
#     print("Кратно")
# else:
#     print("Нет")