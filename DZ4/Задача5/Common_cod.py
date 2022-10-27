import os
os.system('cls||clear')

from Read_file import my_read
from Del_probel import del_probel
from Posle_ravno import posle_ravno
from Pered_ravno import pered_ravno
from Slovar import slovar
from Write_mnogochlen import write_mnogochlen
from Write_file import write_file


# Даны два многочлена в виде строк.

str1 = my_read("file1.txt")
str2 = my_read("file2.txt")

print(str1)
print(str2)


# Удаляем пробелы из строки.
new_str1 = del_probel(str1)
new_str2 = del_probel(str2)

print(new_str1)
print(new_str2)

# Суума элементов после равно

sum_mnogochlen = int(posle_ravno(new_str1)) + int(posle_ravno(new_str2))

print(sum_mnogochlen)

# Берём то, что стоит слева от равно и делим по знаку +.
my_list1 = pered_ravno(str1).split("+")
my_list2 = pered_ravno(str2).split("+")

print(my_list1)
print(my_list2)


# Делим каждый элемент по x^ и вносим данные в словарь.

my_dict = {}
slovar(my_list1, my_list2)

# Сортировка словаря по убыванию ключей, с предварительной записью в кортежи.

sort_dict = dict(sorted(my_dict.items(), reverse=True))

# Запись суммарного многочлена в строку.

if sum_mnogochlen != 0:   
    final_str = write_mnogochlen(sort_dict)[:-2] + f"- {sum_mnogochlen}" + " = 0"
else:
    final_str = write_mnogochlen(sort_dict)[:-2] + " = 0"

print(final_str)

# Записываем результат в новый файл.

write_file("result_file.txt",final_str)