# Напишите программу, которая на вход принимает 2 числа (две позиции).
# Задайте список из N элементов, заполненный числами в промежутке от -N до N.
# Найдите произведение элементов, находящихся в позицияз 1 и 2

# Напишите программу, которая на вход принимает 2 числа (две позиции).
pos1 = int(input("Введите позицию 1: "))
pos2 = int(input("Введите позицию 2: "))

# Задайте список из N элементов, заполненный числами в промежутке от -N до N.

n = int(input("Введите число N: "))
list = range(-n,n + 1)
for i in list:
    print(i, end = " ")
print(" ")

# Найдите произведение элементов, находящихся в позицияз 1 и 2

res = list[pos1] * list[pos2]
print(res)