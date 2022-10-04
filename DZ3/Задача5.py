# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def fibonacci_back(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_back(n-2) - fibonacci_back(n-1))

n = int(input('Введите число: '))

fibo_series = []

for i in range(0, n):
    fibo_series.append(fibonacci(i))

for i in range(1, n):
    fibo_series.insert(0,fibonacci_back(i))

print(fibo_series)