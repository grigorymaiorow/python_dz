# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import os
os.system('cls||clear')

def input_number():
    while True:
        number = input("Введите число: ")
        try:
            num = float(number)
            return num
        except:
            print("Вы ввели не число. Попробуйте снова.")

my_list = []
new_list = []

for num in range(5):  
    num = input_number()
    my_list.append(num)
print(my_list)

for i in range(len(my_list)):
    count = 0
    for j in range(len(my_list)):
        if my_list[i] == my_list[j]:
            count += 1
    if count  <= 1:
        new_list.append(my_list[i])
            
print(new_list)