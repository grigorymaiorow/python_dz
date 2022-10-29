# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример: ggggggghhhhhhhshffffffggtttt44444ooooooollllllo --> 7g7h1s1h6f2g4t547o6l1o --> ggggggghhhhhhhshffffffggtttt44444ooooooollllllo

import os
os.system('cls||clear')

my_str = "ggggggghhhhhhhshffffffggtttt44444ooooooollllllo"
myData = list(my_str)
count = 1
myNewData = []


def compression (myData,myNewData,count):
    for index in range(1, len(myData) ):
        if myData[index-1] == myData[index] and index != len(myData) - 1 :
            count += 1
        elif myData[index-1] != myData[index] and index != len(myData) - 1:
            myNewData.append(count)
            myNewData.append(myData[index-1])
            count = 1
        elif myData[index-1] != myData[index] and index == len(myData) - 1:
            myNewData.append(count)
            myNewData.append(myData[index-1])
            count = 1
            myNewData.append(count)
            myNewData.append(myData[index])
        elif myData[index-1] == myData[index] and index == len(myData) - 1:
            count += 1
            myNewData.append(count)
            myNewData.append(myData[index])
    return ''.join(map(str,myNewData))


m_lst = compression (myData,myNewData,count)
new_str = " "

def recovery(new_str, m_lst):

    for i in range(len(m_lst)):

        if m_lst[i].isdigit() and new_str[-1] == m_lst[i]:
            continue
        
        elif m_lst[i].isdigit():
            new_str += int(m_lst[i]) * m_lst[i+1]
            
        elif not m_lst[i].isdigit() and new_str[-1] == m_lst[i]:
            continue

        else:
            new_str += m_lst[i]

    return new_str[1:] 
    

print("Исходные данные: " + my_str)
print("Сжатые данные: " + m_lst)
print("Восстановленные данные: " + recovery(new_str, m_lst))