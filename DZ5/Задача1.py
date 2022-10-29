# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Текст находится в файле. Его надо считать, текст исправить, исправленный текст записать в новый файл.

with open("file.txt", "r") as text_file:
    text = text_file.read()

res = filter(lambda x: 'абв' not in x,text.split())
n_res = ' '.join(res)

with open("n_file.txt", "w") as n_text_file:
    n_text_file.writelines(n_res)
