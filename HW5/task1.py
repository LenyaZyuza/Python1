# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии. >


def Degree(num, deg):
    if (deg == 1):
        return (num)
    if (deg != 1):
        return (num * Degree(num, deg - 1))
num = int(input("Введите число: "))
deg = int(input("Введите степень числа: "))
print("Результат возведения в степень =", Degree(num, deg))