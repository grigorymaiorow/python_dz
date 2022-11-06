from step2_proverka_polya import proverka_polya
from step2_proveka_znacheniya import proverka_znacheniya

def new_structure():
    my_dict = {}

    while len(my_dict) != 9:
        p = proverka_polya()
        if p == "":
            break

        while p in my_dict:
            print("Эта ячейка уже занята.")
            p = proverka_polya()

        z = proverka_znacheniya()
        if z == "":
            break

        my_dict[f"{p}"] = z


    my_dict = dict(sorted(my_dict.items()))
    return my_dict

new_structure()