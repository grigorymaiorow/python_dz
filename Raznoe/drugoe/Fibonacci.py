import os
os.system('cls||clear')


# Var1_while
# f1 = 0
# f2 = 1
# list = [f1,f2]
# n = int(input("Введите число: "))
# while n >= 0:
#     f1, f2 = f2, f1 + f2
#     # f_sum = f1 + f2
#     # f1 = f2
#     # f2 = f_sum
#     n -= 1
#     list.append(f2)
# print(list)


# Var2_for
# f1 = 0
# f2 = 1
# n = int(input("Введите число: "))
# print(f1, f2, end = " ")

# for _ in range(2,n):
#     f1, f2 = f2, f1 + f2
#     print(f2, end = " ")



# Var3_recursion
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))

# n = int(input('Введите число: '))

# fibo_series = []

# for i in range(0, n):
#     fibo_series.append(fibonacci(i))

# print(fibo_series)



# Var4_recursion_and_back
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