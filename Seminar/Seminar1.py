# Задача1
# Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

# a = int(input('Введите первое число '))
# b = int(input('Введите второе число '))
# if a**2 == b or b**2 == a:
#     print('Одно число является квадратом другого')
# else:
#     print('Числа не взаимные квадраты')


# Задача2
# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.

# m = []
# for i in range(3):
#     m.append(int(input('Введите число: ')))
# print(m)
# max = m[0]

# if m[i] >= max:
#     max = m[i]
# print("Максимальное число ")
# print(max)


# Задача3
# Напишите программу, которая будет на вход принимать число N и
# выводить числа от -N до N

# n = int(input('Введите число N '))
# for i in range(-n,n+1):
#     print(i, end = ' ')


# Задача4
# Напишите программу, которая будет принимать на вход дробь и
# показывать первую цифру дробной части числа.

# a = float(input('Введите дробь '))
# b = int((a*10)%10)
# if b > 0:
#     print(b)
# else:
#     print('нет')


# Задача5
# Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

# num = int(input('Введите число '))
# print(((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and num % 30 != 0)

