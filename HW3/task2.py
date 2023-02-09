#  Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#     Будем считать, что на вход подается только одно слово, которое содержит либо
#     только английские, либо только русские буквы.

point_1 = ['А','В','Е','И','Н','О','Р','C','Т','A','E','I','O','U','L','N','S','T','R']
point_2 = ['Д','К','Л','М','П','У','D','G']
point_3 = ['Б','Г','Ё','Ь','Я','B','C','M','P']
point_4 = ['Й','Ы','F','H','V','W','Y']
point_5 = ['Ж','З','Х','Ц','Ч','K']
point_8 = ['Ш','Э','Ю','J','X']
point_10 = ['Ф','Щ','Ъ','Q','Z']

word = input("Введите слово: ")
word = word.upper()

words = list(word)

print(word.title())

count = 0
for i in words:
    if i in point_1:
        count += 1
    elif i in point_2:
        count += 2
    elif i in point_3:
        count += 3
    elif i in point_4:
        count += 4
    elif i in point_5:
        count += 5
    elif i in point_8:
        count += 8
    elif i in point_10:
        count += 10

print(count)
