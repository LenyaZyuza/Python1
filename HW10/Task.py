import sys

def initial_phonebook():
	rows, cols = int(input("Введите количество контактов: ")), 5
	
	phone_book = []
	print(phone_book)
	for i in range(rows):
		print("\nВведите контактные %d данные:" % (i+1))
		print("Примечание: * указывает на обязательные поля")
		print("....................................................................")
		temp = []
		for j in range(cols):
					
			if j == 0:
				temp.append(str(input("Введите name*: ")))
				if temp[j] == '' or temp[j] == ' ':
					sys.exit(
						"Имя является обязатеным полем. Процесс завершается из-за его отсутствия...")
					
			if j == 1:
				temp.append(int(input("Введите номер*: ")))
				
			if j == 2:
				temp.append(str(input("Введите адрес электроной почты: ")))
				if temp[j] == '' or temp[j] == ' ':
					temp[j] = None
					
			if j == 3:
				temp.append(str(input("Введите дату рождения(dd/mm/yy): ")))
				if temp[j] == '' or temp[j] == ' ':
				
					temp[j] = None
			if j == 4:
				temp.append(
					str(input("Введите категорию(Family/Friend/Work/Other): ")))
				if temp[j] == "" or temp[j] == ' ':
					temp[j] = None
					
		phone_book.append(temp)

	print(phone_book)
	return phone_book

def menu():
	print("********************************************************************")
	print("\t\t\tТЕЛЕФОННЫЙ СПРАВОЧНИК", flush=False)
	print("********************************************************************")
	print("\tТеперь вы можете выполнять следующие опервции:\n")
	print("1. Добавить контакт")
	print("2. Удалить существующий контакт")
	print("3. Удалить все контакты")
	print("4. Поиск контакта")
	print("5. Показать все контакты")
	print("6. Закрыть справочник")

	choice = int(input("Введите номер действия, который хотите совершить: "))
	
	return choice

def add_contact(pb):
	dip = []
	for i in range(len(pb[0])):
		if i == 0:
			dip.append(str(input("Введите name: ")))
		if i == 1:
			dip.append(int(input("Введите номер: ")))
		if i == 2:
			dip.append(str(input("Введите адрес электронной почты: ")))
		if i == 3:
			dip.append(str(input("Введите дату дня рождения(dd/mm/yy): ")))
		if i == 4:
			dip.append(
				str(input("Введите категорию(Family/Friend/Work/Other): ")))
	pb.append(dip)
	return pb

def remove_existing(pb):
	query = str(
		input("Введите имя контакта, который хотите удалить: "))
	
	temp = 0
	
	for i in range(len(pb)):
		if query == pb[i][0]:
			temp += 1
			print(pb.pop(i))
			print("Этот запрос был удален")
			return pb
	if temp == 0:
		print("Ошибка, вы ввели недопустивый запрос .\
	Пожалуйста перепроверье и повторите попытку позже.")
		return pb

def delete_all(pb):
	return pb.clear()

def search_existing(pb):
	choice = int(input("Введите критерии поиска\n\n\
	1. Name\n2. Номер\n3. Адрес электронной почты\n4. Дата рождения\n5. Категория(Family/Friend/Work/Other)\
	\nПожалуйста введите: "))
	
	temp = []
	check = -1
	
	if choice == 1:
		query = str(
			input("Введите name контакта, который вы хотите найти: "))
		for i in range(len(pb)):
			if query == pb[i][0]:
				check = i
				temp.append(pb[i])
				
	elif choice == 2:
		query = int(
			input("Введите номер контакта, который вы хотите найти: "))
		for i in range(len(pb)):
			if query == pb[i][1]:
				check = i
				temp.append(pb[i])
				
	elif choice == 3:
		query = str(input("Введите адрес электронной почты\
		контакта, который вы хотите найти: "))
		for i in range(len(pb)):
			if query == pb[i][2]:
				check = i
				temp.append(pb[i])
				
	elif choice == 4:
		query = str(input("Введите дату рождения (только в формате dd/mm/yy)\
			контакта, который вы хотите найти: "))
		for i in range(len(pb)):
			if query == pb[i][3]:
				check = i
				temp.append(pb[i])
				
	elif choice == 5:
		query = str(
			input("Введите категорию контакта, который вы хотите найти:: "))
		for i in range(len(pb)):
			if query == pb[i][4]:
				check = i
				temp.append(pb[i])
		
	else:
		print("Неверные категории поиска")
		return -1
	
	if check == -1:
		return -1
	else:
		display_all(temp)
		return check

def display_all(pb):
	if not pb:
		print("Список пуст: []")
	else:
		for i in range(len(pb)):
			print(pb[i])

def thanks():
	print("********************************************************************")
	print("Спасибо, что воспользовались данным телефонным справочником.")
	print("Возвращайтесь снова!")
	print("********************************************************************")
	sys.exit("До свидвния, всего самого наилучшего!")

print("....................................................................")
print("Здравствуйте, дорогой пльзователь, добро пожаловать в телефонный справочник!")
print("Теперь вы можете приступить к работе.")
print("....................................................................")

ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
	ch = menu()
	if ch == 1:
		pb = add_contact(pb)
	elif ch == 2:
		pb = remove_existing(pb)
	elif ch == 3:
		pb = delete_all(pb)
	elif ch == 4:
		d = search_existing(pb)
		if d == -1:
			print("Контакт не существует. Попробуйте еще раз. ")
	elif ch == 5:
		display_all(pb)
	else:
		thanks()
