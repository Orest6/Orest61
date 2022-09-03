a = input('Введите первое число ')
b = input('Введите второе число ')
try:
    int(a)/int(b)
except ValueError:
    print('Вводите только числа')
try:
    a+int(b)
except TypeError:
    print('Разные типы данных')