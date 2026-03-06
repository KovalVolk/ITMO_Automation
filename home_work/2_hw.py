# Задача №1

def task_1()-> None:

     a: int = 3
     b: float = 3.5
     c: str = 'строка'
     d: list = [1, 2]
     e: bool = True

     print(f'Тип a:, {type(a)}')
     print(f'Тип b:, {type(b)}')
     print(f'Тип c:, {type(c)}')
     print(f'Тип d:, {type(d)}')
     print(f'Тип e:, {type(e)}')

task_1()


# Задача №2

def task_2()-> None:

    a = [1, 2, 3, 5, 8, 13, 21]

    print(f'\nПервые три значения:, {a[:3]}')

task_2()


# Задача №3

x: int = 5

def task_3(x)->int:
    return x*x

print(task_3(x))
