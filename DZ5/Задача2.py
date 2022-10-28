# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import os
os.system('cls||clear')

import random

count = 220


# Игра человек - человек (без проверки "на дурака")

while count > 0:
    game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
    while game_first not in range(1,29):
        game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
    
    count -= game_first
    print("Осталось " f"{count}" " конфет")
    
    if count <= 0:
        print("Победил game_first")
        break

    else:
        game_second = int(input("Сколько конфет хотите забрать, game_second ?: "))
        while game_second not in range(1,29):
            game_second = int(input("Сколько конфет хотите забрать, game_second ?: "))
        count -= game_second
        print("Осталось " f"{count}" " конфет")
        if count <= 0:
            print("Победил game_second")
            break



# Игра с ботом

# number_input = int(input("Ведите '1' если хотите ходить первым или  '2' если первым ходит бот: "))
# while number_input not in range(1,3):
#     number_input = int(input("Ведите '1' если хотите ходить первым или  '2' если первым ходит бот "))

# while count > 0:

#     if number_input == 1:
#         game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
#         while game_first not in range(1,29):
#             game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
        
#         count -= game_first
#         print("Осталось " f"{count}" " конфет")
        
#         if count <= 0:
#             print("Поздравляю, Вы победили")
#             break
#         else:
#             game_bot = random.randint(1,28)
#             count -= game_bot
#             print("game_bot взял " f"{game_bot}" " конфет")
#             print("Осталось " f"{count}" " конфет")
            
#             if count <= 0:
#                 print("Победил game_bot")
#                 break


#     else:
#         game_bot = random.randint(1,28)
#         count -= game_bot
#         print("game_bot взял " f"{game_bot}" " конфет")
#         print("Осталось " f"{count}" " конфет")
#         if count <= 0:
#             print("Победил game_bot")
#             break

#         else:
#             game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
#             while game_first not in range(1,29):
#                 game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
            
#             count -= game_first
#             print("Осталось " f"{count}" " конфет")
            
#             if count <= 0:
#                 print("Поздравляю, Вы победили")
#                 break



# Игра с умным ботом

# number_input = int(input("Ведите '1' если хотите ходить первым или '2' если первым ходит бот: "))
# while number_input not in range(1,3):
#     number_input = int(input("Ведите '1' если хотите ходить первым или '2' если первым ходит бот "))

# while count > 0:

#     if number_input == 1:
#         game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
#         while game_first not in range(1,29):
#             game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
        
#         count -= game_first
#         print("Осталось " f"{count}" " конфет")
        
#         if count <= 0:
#             print("Поздравляю, Вы победили")
#             break

#         else:
#             game_bot = count - count // 29 * 29
#             if game_bot == 0:
#                 game_bot = random.randint(1,28)
#             count -= game_bot
#             print("game_bot взял " f"{game_bot}" " конфет")
#             print("Осталось " f"{count}" " конфет")
            
#             if count <= 0:
#                 print("Победил game_bot")
#                 break


#     else:
#         game_bot = count - count // 29 * 29
#         count -= game_bot
#         if game_bot == 0:
#                 game_bot = random.randint(1,28)
#         print("game_bot взял " f"{game_bot}" " конфет")
#         print("Осталось " f"{count}" " конфет")

#         if count <= 0:
#             print("Победил game_bot")
#             break

#         else:
#             game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
#             while game_first not in range(1,29):
#                 game_first = int(input("Сколько конфет хотите забрать, game_first ?: "))
            
#             count -= game_first
#             print("Осталось " f"{count}" " конфет")

#             if count <= 0:
#                 print("Поздравляю, Вы победили")
#                 break
