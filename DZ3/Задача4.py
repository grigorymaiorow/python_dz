# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def input_numbers ():
    while True:
        num = input('введите число - ')
        try:
            numbers = int(num)
            return numbers
        except:
            print('не число')

number = input_numbers()

my_list = [1]

if number == 0:
    print(0)
else:
    while number > 1:
        ost = number % 2
        number = number // 2
        my_list.insert(1,ost)
    print("".join(map(str, my_list)))

