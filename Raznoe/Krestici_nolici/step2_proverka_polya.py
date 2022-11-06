def proverka_polya():

    while True:

        # Приглашение к вводу
        data = input("Введите ячейку в виде [x1y1]: ")

        # Досрочное завершение игры игроком
        if data == "": 
            data = input("Вы уверены, что хотети закончить игру. Если да, нажмите [enter]. Если нет, то введите любой символ: ")
            if data == "":
                print("Игра закончена.")
                break
            else:
                data = input("Введите ячейку в виде [x1y1]: ")

        # Проверка ввёдённого
        if len(data) == 4:
            if data[0] != "x" or not data[1].isdigit() or 3 < int(data[1]) or int(data[1]) < 1 or data[2] != "y" or not data[3].isdigit() or 3 < int(data[3]) or int(data[3]) < 1:
                print("Вы ввели неверные данные. Попробуйте ещё раз: ")
            else:
                data = data
                break
        
    return data