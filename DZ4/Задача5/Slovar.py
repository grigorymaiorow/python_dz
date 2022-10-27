# Делим каждый элемент по x^ и вносим данные в словарь.

my_dict = {}


def proverka(my_list1,i):
    if "x^" not in my_list1[i] and "x" in my_list1[i]:
        my_list1[i] = my_list1[i].replace("x",f"x^{len(my_list1)- (i+1)}")
        
    if "x" not in my_list1[i]:
        my_list1[i] = my_list1[i] + "x^0"
    return my_list1[i]


def slovar(my_list1,my_list2):

        
    for i in range(len(my_list1)):

        proverka(my_list1,i)

        chast = my_list1[i].split("x^")

        my_dict[chast[1]] = int(chast[0])

    keys = my_dict.keys()


    for j in range(len(my_list2)):

        proverka(my_list2,j)
        
        chasn = my_list2[j].split("x^")
        
        if chasn[1] in keys:
            
            my_dict[chasn[1]] = my_dict[chasn[1]] + int(chasn[0]) 
        
        if chasn[1] not in keys:
            my_dict[chasn[1]] = int(chasn[0])

    return my_dict

