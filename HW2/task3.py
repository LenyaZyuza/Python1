# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input("Введите число: "))

count = 1

while count <= num:
    print(count)
    count *= 2
