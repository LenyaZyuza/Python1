# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

from random import randint

coin = int(input("Введите кол-во монет: "))

tails = 0
eagle = 0

for count in range(1, coin + 1):
    coins = randint(0, 1)
    print(f"Рандомное число - {coins}")
    if coins == 1:
        tails += 1
    else:
        eagle += 1
print(f"Решка = {tails}")
print(f"Орел = {eagle}")
sum_tails = tails
sum_eagle = eagle
if sum_tails < sum_eagle:
    print(f"Число решек, которое надо перевернуть = {sum_tails}")
if sum_tails > sum_eagle:
    print(f"Число орлов, которое надо перевернуть = {sum_eagle}")
if sum_eagle == sum_tails:
    print(f"Равное кол-во переворачиваний = {sum_tails}, {sum_eagle}")