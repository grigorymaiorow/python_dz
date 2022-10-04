# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
new_list = []

# Вариант1
# while len(my_list) > 1 :
#     res = int(my_list[0]) * int(my_list[-1])
#     new_list.append(res)
#     my_list.pop(0)
#     my_list.pop(-1)
# if len(my_list) > 0:
#     new_list.append(my_list[0] **2 )
# print(new_list)

# Вариант2
for i in range(int(len(my_list) / 2 + 0.5)):
    res = int(my_list[i]) * int(my_list[-(i+1)])
    new_list.append(res)
print(new_list)


