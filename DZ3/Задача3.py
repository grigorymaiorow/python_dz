# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

new_list = []
def new (list):
    for i in range (len(my_list)):
        num = my_list[i] - int (my_list[i])
        if num != 0:
            new_list.append(round(num, 5))       # 5 - произвольное число, до которого будет производиться округление
    
    if len(new_list) == 0:
        print("Все числа целые")
    if len(new_list) == 1:
        print("Всего одно дробное число")
    if len(new_list) != 0:
        max_num = max(new_list)
        min_num = min(new_list)
        result = (max(new_list) - min(new_list))
        print("Разница между максимальным и минимальным значением дробной части элементов равна", result)

new(my_list)