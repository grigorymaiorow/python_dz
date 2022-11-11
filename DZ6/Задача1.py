# 1. Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200. Использовать comprehensions

N = 50
my_list = [i for i in range(50) if i%2 != 0 and i*i < 200]
print(my_list)