# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

d = int(input('Input d '))
a = [0]*d
a[0] = int(input('Input a[0] '))
n = int(input('Input n '))
print(a[0],end=' ')
for i in range(1,d):
    a[i]= a[i-1]+n
    print(a[i],end=' ')