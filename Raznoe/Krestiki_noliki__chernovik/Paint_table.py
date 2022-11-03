from prettytable import PrettyTable

def draw_file(struct_dict):
    my_table = PrettyTable()
    my_table.field_names = ["Y\X", "X1", "X2", "X3"]
    my_table.add_rows(
        [
            ["Y1", f"{struct_dict['x1y1']}",f"{struct_dict['x2y1']}",f"{struct_dict['x3y1']}"],
            ["--", "--","--","--"],
            ["Y2", f"{struct_dict['x1y2']}",f"{struct_dict['x2y2']}",f"{struct_dict['x3y2']}"],
            ["--", "--","--","--"],
            ["Y3", f"{struct_dict['x1y3']}",f"{struct_dict['x2y3']}",f"{struct_dict['x3y3']}"],
        ]
    )
    print(my_table)
























# Второй вариант заполнения (для себя)
# from texttable import Texttable
# myt_table = Texttable()
# my_list = list(struct_dict.values())
# myt_table.add_rows([["1","2","3"], my_list[:3], my_list[3:6], my_list[6:9]])
# print(myt_table.draw())