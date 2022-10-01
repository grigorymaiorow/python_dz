# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11




# Способ1
n = input("Введите число = ").replace('.', '').replace('-', '')
while not n.isdigit():
    n = input("Введите число = ").replace('.', '').replace('-', '')
n = list(n)
my_sum = sum(list(map(int,n)))
print(my_sum)

# Способ2
# n = input("Введите число = ") 
# sum = 0
# for i in n:
#     if i.isdigit():
#         sum += int(i)
# print(sum)