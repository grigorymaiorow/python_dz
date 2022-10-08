import os
os.system('cls||clear')
# Вычислить число c заданной точностью

def input_numbers():

    while True:
        num = input('Введите число: ')
        try:
            number = float(num)
            return number
        except:
            print('Вы ввели не число. Попробуйте снова.')

def input_count():
    while True:
        num = input('Введите точность округления: ')
        try:
            numbers = int(num)
            return numbers
        except:
            print('Вы ввели не число. Попробуйте снова.')

number = input_numbers()
count = input_count()

print(f'{number:.{count}f}')