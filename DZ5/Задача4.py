# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример: ggggggghhhhhhhshffffffggtttt44444ooooooollllllo--> 7g7h1s1h6f2g4t547o6l1o

data1 = open('file_with_data.txt', 'r')
myData = []

for line in data1:
    myData.extend(line)
data1.close()
print(myData)
count = 1
myNewData = []
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
print(''.join(map(str,myNewData)))
with open('file_with_newdata.txt', 'w') as data2:
    data2.write(''.join(map(str, myNewData)))