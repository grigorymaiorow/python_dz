# Imports.
import os
from random import choice
from prettytable import PrettyTable


os.system('cls||clear')

# Структура хранения данных и её случайное заполнение.
struct_dict = \
    {
        'x1y1' : '' , 'x2y1' : ''  , 'x3y1' : '' ,
        'x1y2' : '' , 'x2y2' : ''  , 'x3y2' : '' ,
        'x1y3' : '' , 'x2y3' : ''  , 'x3y3' : ''
    }

for key in struct_dict:
    struct_dict[key] = choice('X O')
print(struct_dict)


# Прорисовка таблицы с заполнение.
my_table = PrettyTable()

my_table.field_names = ["Y\X", "X1", "X2", "X3"]
my_table.add_row(["Y1", f"{struct_dict['x1y1']}",f"{struct_dict['x2y1']}",f"{struct_dict['x3y1']}"])
my_table.add_row(["--", "--","--","--"])
my_table.add_row(["Y2", f"{struct_dict['x1y2']}",f"{struct_dict['x2y2']}",f"{struct_dict['x3y2']}"])
my_table.add_row(["--", "--","--","--"])
my_table.add_row(["Y3", f"{struct_dict['x1y3']}",f"{struct_dict['x2y3']}",f"{struct_dict['x3y3']}"])

print(my_table)