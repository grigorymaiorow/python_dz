# Задайте список из n чисел последовательности (1 + 1/i)**i и выведите на экран их сумму.

n = int(input('Введите число: '))
my_list = []

for i in range(1, n+1):
    my_list.append(round((1+1/i)**i,2))
print(my_list)
print(sum(my_list))