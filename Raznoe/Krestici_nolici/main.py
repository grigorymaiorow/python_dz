import os
from step2_structure_data import new_structure
from step1_draw_file import draw_file
from step1_structure_data import filling
from step2_who_win import who_win

os.system('cls||clear')

my_dict = {'x1y1' : '', 'x2y1' : '', 'x3y1' : '', 'x1y2' : '', 'x2y2' : '', 'x3y2' : '', 'x1y3' : '', 'x2y3' : '', 'x3y3' : ''}
draw_file(filling(" "))

i = 0
count = 0

while i < 9:

    draw_file(new_structure(my_dict,count))
    i += 1
    count += 1


if who_win(my_dict) == "0":
    print("Победили нолики")
elif who_win(my_dict) == "x":
    print("Победили крестики")
else: 
    print("Ничья")
