# Реализуйте алгоритм перемешивания списка.
import random
my_list = [56, 89, 56, 34, 9, 6]
for i, elem in enumerate(my_list):
    a =  random.randint(0,len(my_list) -1)
    if i != a:
        elem,my_list[a] = my_list[a],elem
        print(elem, my_list[a])
print(my_list)