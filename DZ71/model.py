

def import_file(name_file,text):
    with open(f"{name_file}", "a") as file_import:
        file_import.write(text)


def export_file(name_file,text):
    with open(f"{name_file}", "r") as file_export:

        data = file_export.read()
        data = (data.split("\n"))
        
        elem = text.split(",")

        for i in range(len(data)):
            meaning = data[i].split(",")

            if meaning[0] == elem[0] and meaning[1] == elem[1]:
                print("Вы искали: " + data[i])
                break
        else: print("К сожалению, таких данных нет.")









 