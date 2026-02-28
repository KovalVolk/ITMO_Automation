# Задача №1

def task_1(x, y):
    if x > y:
        print(f'Наибольшее число: {x}')
    elif x == y:
        print(f'Числа равны')
    else:
        print(f'Наибольшее число: {y}')

task_1(6, 9)

# Задача №2

def task_2(a, b):
    if abs(a - b) == 135:
        print('YES')
    else:
        print('NO')

task_2(535, 400)

# Задача №3

def task_3(month):
    if month == 1 or month == 2 or month == 12:
        print('Зима')
    elif month in range(3,6):
        print('Весна')
    elif month in range(6,9):
        print('Лето')
    elif month in range(9,12):
        print('Осень')
    else: print('Введите номер месяца от 1 до 12')

task_3(9)

# Задача №4

def task_4(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else: print('No')

task_4(19, 12, 15)




