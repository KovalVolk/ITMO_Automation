# Задача №1

def task_1(a, b, c, d, e)->int:
    return a*a
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

print(task_1(a,b,c,d,e))

# Задача №2

a:list = [1, 2, 3, 5, 8, 13, 21]
print("a[0:3] = ", a[0:3])

def task_2(a:list)->int:
    return len(a)

print(task_2([1,2,3,5,8]))

# Задача №3

def task_3(x):
    return x*x
print(task_3(4))

x: int = 5

def task_3(x)->int:
    return x*x

print(task_3(x))
