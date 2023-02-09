# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint 

len_list = int(input("Введите желаемую длину списка: "))
search = int(input("Введите искомое число Х: "))
my_list = []
value_search = 0

for item in range(len_list):
    my_list_2 = randint(1,100)
    my_list.append(my_list_2)
for item in my_list:
    if item == search:
        value_search += 1
print(my_list)
if value_search >= 1:
    print(f"Число {search} встречается {value_search} раз(а).") # До этого момента включительно написал все сам.
else:
    print(f"Максимально близкое к {search} это {min(my_list, key=lambda x:abs(x-search))}") # А вот эту конструкцию, честно говоря, сам не мог сообразить, как найти максимально близкое значение, нашел ее на Stackoverflow.