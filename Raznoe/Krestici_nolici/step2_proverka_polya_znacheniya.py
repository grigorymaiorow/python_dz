def proverka_polya():

    while True:

        data = input("Введите ячейку в виде [x1y1]: ")

        if data == "": 
            data = input("Вы уверены, что хотети закончить игру. Если да, нажмите [enter]. Если нет, то введите любой символ: ")
            if data == "":
                break
            else:
                data = input("Введите ячейку в виде [x1y1]: ")

        if len(data) == 4:
            if data[0] != "x" or not data[1].isdigit() or 3 < int(data[1]) or int(data[1]) < 1 or data[2] != "y" or not data[3].isdigit() or 3 < int(data[3]) or int(data[3]) < 1:
                print("Вы ввели неверные данные. Попробуйте ещё раз: ")
            else:
                data = data
                break
        
    return data
















# def proverka_znacheniya():

#     while True:

#         el = input("Введите значение 'x' или '0' :  ")

#         if el == "": 
#             el = input("Вы уверены, что хотети закончить игру. Если да, нажмите [enter]. Если нет, введите любой символ: ") 
#             if el == "":
#                 break
#             else:
#                 el = input("Введите значение 'x' или '0' :  ")
      
#         if len(el) == 1:
#             if el != "x" and el !=  "0" and el !=  "o":
#                 print("Вы ввели неверные данные. Попробуйте ещё раз: ")
#             else:
#                 el = el
#                 break
#     return el