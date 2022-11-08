from step2_proverka_polya import proverka_polya
from step2_proveka_znacheniya import proverka_znacheniya

# def new_structure():
#     my_dict = {'x1y1' : '', 'x2y1' : '', 'x3y1' : '', 'x1y2' : '', 'x2y2' : '', 'x3y2' : '', 'x1y3' : '', 'x2y3' : '', 'x3y3' : ''}

#     while len(my_dict) != 18:
#         p = proverka_polya()
#         if p == "":
#             break

#         while my_dict.get(f"{p}") != '':
#             print("Эта ячейка уже занята.")
#             p = proverka_polya()

#         z = proverka_znacheniya()
#         if z == "":
#             break

#         my_dict[f"{p}"] = z


#     my_dict = dict(sorted(my_dict.items()))
#     return my_dict


# new_structure()


# def new_structure(my_dict):
    
#     p = proverka_polya()

#     while p == "": 
#         break

#     else:
#         while my_dict.get(f"{p}") != '':
#             print("Эта ячейка уже занята.")
#             p = proverka_polya()

#             z = proverka_znacheniya()
#             while z == "":
#                 break

#             else: my_dict[f"{p}"] = z

    
#     return my_dict


def new_structure(my_dict):
    
    p = proverka_polya()

    if p == "": 
        print("Игра закончена.")
        quit()

    while my_dict.get(f"{p}") != '':
        print("Эта ячейка уже занята.")
        p = proverka_polya()

    z = proverka_znacheniya()
    if z == "":
        quit()

    my_dict[f"{p}"] = z

    
    return my_dict

