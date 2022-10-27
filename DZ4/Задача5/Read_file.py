# Считать два файла и забрать из каждого по многочлену.

def my_read(data_name):

    with open (data_name, 'r') as data:
        stroka = data.read()
    return stroka
