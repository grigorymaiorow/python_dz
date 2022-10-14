# #Создайте программу для игры в ""Крестики-нолики"".

Задача не решена

# import os
# os.system('cls||clear')


# def field(moves):
#     print(f"    X1    X2   X3  ")
#     print(f"Y1  {moves['y1']['x1']}  |  {moves['y1']['x2']}  | {moves['y1']['x3']}  ")
#     print("  -----+-----+-----")
#     print(f"Y2  {moves['y2']['x1']}  |  {moves['y2']['x2']}  | {moves['y2']['x3']}  ")
#     print("  -----+-----+-----")
#     print(f"Y3  {moves['y3']['x1']}  |  {moves['y3']['x2']}  | {moves['y3']['x3']}  ")
    

# def wins(moves):
#     if ((moves['y1']['x1'] == moves['y1']['x2'] == moves['y1']['x3']
#             or moves['y1']['x1'] == moves['y2']['x1'] == moves['y3']['x1']
#             or moves['y1']['x1'] == moves['y2']['x2'] == moves['y3']['x3'])
#             and moves['y1']['x1'] != ' '):
#         return moves['y1']['x1']
#     elif ((moves['y2']['x1'] == moves['y2']['x2'] == moves['y2']['x3']
#            or moves['y1']['x2'] == moves['y2']['x2'] == moves['y3']['x2']
#            or moves['y1']['x3'] == moves['y2']['x2'] == moves['y3']['x1'])
#           and moves['y2']['x2'] != ' '):
#         return moves['y2']['x2']
#     elif ((moves['y3']['x1'] == moves['y3']['x2'] == moves['y3']['x3']
#            or moves['y1']['x3'] == moves['y2']['x3'] == moves['y3']['x3'])
#           and moves['y3']['x3'] != ' '):
#         return moves['y3']['x3']
#     return False


# def move(symbol, moves, player):
#     print(player[1], player[-1])
#     if player[1] == '1':
#         if player[-1] == '1':
#             moves['y1']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y1']['x2'] = symbol
#         else:
#             moves['y1']['x3'] = symbol
#     elif player[1] == '2':
#         if player[-1] == '1':
#             moves['y2']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y2']['x2'] = symbol
#         else:
#             moves['y2']['x3'] = symbol
#     else:
#         if player[-1] == '1':
#             moves['y3']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y3']['x2'] = symbol
#         else:
#             moves['y3']['x3'] = symbol
#     return moves


# moves_out = {
#     'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
# }

# field(moves_out)

# number_players = int(input('Введите количество игроков (1/2): '))
# count_move = 0

# if number_players == 2:
#     win = False
#     while not win:
#         count_move += 1
#         player_out = input('Введите координаты хода(пример - y2x3): ')
#         if count_move % 2:
#             symbol_out = 'X'
#         else:
#             symbol_out = 'O'
#         moves_out = move(symbol_out, moves_out, player_out)
#         field(moves_out)
#         win = wins(moves_out)

#     print('На {count_move} ходу победили "{win}"')

