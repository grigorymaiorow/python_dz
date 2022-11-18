from view import input_data1
from view import input_data2
from view import input_name_file
from view import action
from model import import_file
from model import export_file


def main_file():
    name_file = input_name_file()
    actions = action()

    if actions == "1":
        text = input_data1()
        import_file(name_file,text)
    

    if actions == "2":

        text = input_data2()
        export_file(name_file,text)      
