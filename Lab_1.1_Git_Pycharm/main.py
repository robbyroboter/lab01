# Функция для нахождения НОД с помощью алгоритма Евклида
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Присваиваем b значение остатка от деления a на b
    return a

# Ввод двух целых чисел
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# Вычисляем НОД
result = gcd(num1, num2)

# Выводим результат
print(f"Наибольший общий делитель (НОД) чисел {num1} и {num2} = {result}")

