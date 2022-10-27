# Записываем результат в новый файл.


def write_file(data_name, my_str):

    with open (data_name, 'w') as data:
        data.write(my_str)

