

def input_data1():

    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    description = input("Введите описание: ")

    return f"{surname},{name},{phone_number},{description}\n"


def input_data2():

    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")

    return f"{surname},{name}"


def input_name_file():
    return input("Введите имя файла, с которым хотите работать: ") 


def action():
    return input("Что Вы хотите сделать? Введите 1, если хотите записать данные в файл, или 2, если хотите прочитать данные из файла. ")
