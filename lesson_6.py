# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('введите a1: '))
d = int(input('введите d: '))
n = int(input('введите n: '))

list = []

for i in range (1, n+1):
    an = a1 + (i-1) * d
    list.append(an)

print(list)