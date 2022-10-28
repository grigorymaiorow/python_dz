# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

with open("file_dz5.1.txt", "r") as text_file:
    text = text_file.read()

res = filter(lambda x: 'абв' not in x,text.split())
print(' '.join(res))

