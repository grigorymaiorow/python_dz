# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = 12345

# Вариант1
my_list = []
for i in range(2,n+1):
    j = 2
    count = 0
    while j < i + 1:
        if i % j == 0:
            count += 1
        j += 1
    if count < 2 and n % i == 0:
            my_list.append(i)


print(my_list)          


# Вариант2
i = 2
multipliers = [1]
while i * i <= user_number:
    while user_number % i == 0:
        multipliers.append(i)
        user_number = user_number // i
    i = i + 1
if user_number > 1:
    multipliers.append(user_number)
print(multipliers)
