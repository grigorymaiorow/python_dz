from step2_proverka_polya_znacheniya import proverka_polya


def new_structure(my_dict, count):

    
    p = proverka_polya()

    if p == "": 
        print("Игра закончена.")
        quit()

    while my_dict.get(f"{p}") != '':
        print("Эта ячейка уже занята.")
        p = proverka_polya()

    
    if count % 2 == 0:
        z = "X"
    else:
        z = "0"

    my_dict[f"{p}"] = z

    
    return my_dict

