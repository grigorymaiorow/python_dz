# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import os
os.system('cls||clear')

# Считать два файла и забрать из каждого по многочлену.

def my_read(data_name):

    with open (data_name, 'r') as data:
        stroka = data.read()
    return stroka

# Даны два многочлена в виде строк.

str1 = my_read("file1.txt")
str2 = my_read("file2.txt")

# Удаляем пробелы из строки.


def del_probel(str):
    new_str = str.replace(" ","")
    return new_str

new_str1 = del_probel(str1)
new_str2 = del_probel(str2)


# Делим строку по знаку "=" и складываем значения после него.


def posle_ravno(str):
    res = str.split("=")
    return(res[1])

sum_mnogochlen = int(posle_ravno(new_str1)) + int(posle_ravno(new_str2))

# Берём то, что стоит слева от равно и делим по знаку +.


def pered_ravno(my_str):
    res = my_str.split("=")
    return(res[0])

my_list1 = pered_ravno(str1).split("+")
my_list2 = pered_ravno(str2).split("+")



# Делим каждый элемент по x^ и вносим данные в словарь.

my_dict = {}

def funck(my_list1,my_list2):

    for i in range(len(my_list1)):

        if "x^" not in my_list1[i]:
            my_list1[i] = my_list1[i].replace("x","x^1")

        chast = my_list1[i].split("x^")

        my_dict[chast[1]] = int(chast[0])
    
    print(my_dict)


    keys = my_dict.keys()


    for j in range(len(my_list2)):


        if "x^" not in my_list2[j]:
            my_list2[j] = my_list2[j].replace("x","x^1")
        
        chasn = my_list2[j].split("x^")

        print(chasn)
        
        if chasn[1] in keys:
            
            my_dict[chasn[1]] = my_dict[chasn[1]] + int(chasn[0]) 

        if chasn[1] not in keys:
            my_dict[chasn[1]] = int(chasn[0])
        
funck(my_list1, my_list2)


# Сортировка словаря по убыванию ключей, с предварительной записью в кортежи.

sort_dict = dict(sorted(my_dict.items(), reverse=True))


# Запись суммарного многочлена в строку.


def write_mnogochlen(sort_dict):
    str_mnogochlen = ""
    for k,val in sort_dict.items():
        my_str = f"{val}x^{k}+ "
        str_mnogochlen += my_str
    return str_mnogochlen
    
if sum_mnogochlen != 0:   
    final_str = write_mnogochlen(sort_dict)[:-2] + f"- {sum_mnogochlen}" + " = 0"
else:
    final_str = write_mnogochlen(sort_dict)[:-2] + " = 0"


# Записываем результат в новый файл.

def write_file(data_name):

    with open (data_name, 'w') as data:
        data.write(final_str)

write_file("result_file.txt")


