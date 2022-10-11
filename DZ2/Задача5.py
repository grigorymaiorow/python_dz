# Реализуйте алгоритм перемешивания списка.

import random
my_list = [1,2,3,4,5]
ind_list = []

for i, elem in enumerate(my_list):
    if i in ind_list:
        continue
    ind_list.append(i)
    a = random.randint(0,len(my_list) -1)
    while a in ind_list:
        a = random.randint(0,len(my_list) -1)
        if len(ind_list) == 5:
            break
    else:
        ind_list.append(a)
        if i != a:
            my_list[i],my_list[a] = my_list[a],my_list[i]
print(my_list)

