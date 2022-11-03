## Лямбда

# def sum (x, y):
#     return x+y

# f = sum
# sum = lambda x, y: x+y+1
# f = sum

# def mylt (x, y):
#     return x*y

# def calc(op,a,b):
#     print(op(a,b))
    
# calc(lambda x, y: x+y+1, 3,4)



##list comprehension

## Работа с списками
# list = []
# for i in range(1,21):
#     if (i % 2) == 0:
#         list.append(i)
# print(list)

# list = [i for i in range(1,21) if (i % 2) == 0]
# print(list)


## Кортежи в списках
# list = [(i,i) for i in range(1,21) if (i % 2) == 0]
# print(list)


## Функции в списках
# def f(x):
#     return x**3
# list = [f(i) for i in range(1,21) if (i % 2) == 0]
# print(list)


# map

# li = [x for x in range(1,21)]
# ly = list(map(lambda x:x+10, li))
# print(ly)


# filter

# data = [x for x in range(1,11)]
# res = list(filter(lambda x: not x%2, data))
# print(res)


#  zip

# my_list = [1,2,3]
# array = ['a','б','в']
# mass = [0.1, 0.2, 0.3]

# data = list(zip(my_list, array, mass))
# print(data)


# enumerate

# array = ['a','б','в']
# data = list(enumerate(array))
# print(data)




# Работа с файлами
# my_list = ['1', '2', '3']
# # data = open('file.txt', 'w')
# # data.writelines(my_list)
# # data.close()

# with open('file.txt', 'r') as data:
#     for line in data:
#         print(line)
