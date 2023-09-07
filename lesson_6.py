# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input('введите a1: '))
# d = int(input('введите d: '))
# n = int(input('введите n: '))

# list = []

# for i in range (1, n+1):
#     an = a1 + (i-1) * d
#     list.append(an)

# print(list)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

# from random import randint

numbers = [5, 10, 15, 20, 25, 30]
min_value = 5
max_value = 25

def find_indexes(lst, min_value, max_value):
    indexes = []
    for i in range(len(lst)):
        if lst[i] >= min_value and lst[i] <= max_value:
            indexes.append(i)
    return indexes

result = find_indexes(numbers, min_value, max_value)

print(result)