# Делим каждый элемент по x^ и вносим данные в словарь.

my_dict = {}

def slovar(my_list1,my_list2):

    for i in range(len(my_list1)):

        if "x^" not in my_list1[i]:
            my_list1[i] = my_list1[i].replace("x","x^1")

        chast = my_list1[i].split("x^")

        my_dict[chast[1]] = int(chast[0])
    
    print(my_dict)


    keys = my_dict.keys()


    for j in range(len(my_list2)):


        if "x^" not in my_list2[j]:
            my_list2[j] = my_list2[j].replace("x","x^1")
        
        chasn = my_list2[j].split("x^")

        # print(chasn)
        
        if chasn[1] in keys:
            
            my_dict[chasn[1]] = my_dict[chasn[1]] + int(chasn[0]) 

        if chasn[1] not in keys:
            my_dict[chasn[1]] = int(chasn[0])
        

