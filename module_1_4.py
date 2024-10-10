from dataclasses import replace

my_string = input('В каком городе вы живете: ')
#my_string1 = input('мне ' , ' года')
print('Количество символов в строке:', int(len(my_string)))
print('Вывод строки в нижнем регистре:', my_string.lower())
print('Вывод строки в верхнем регистре:', my_string.upper())
print('Вывод строки без пробелов:' ,my_string .replace(' ' , ''))
print('Вывод первого символа строки:' , my_string[0])
print('Вывод последнего символа строки:' , my_string[-1])