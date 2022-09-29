#Написать функцию, которая просит ввести имя и выводит на экран "Привет и введённое имя".
#Далее написать к функции декоратор, который изменяет функцию и переводит имя в заглавные буквы.
name = input('Введите Ваше имя: ')
def decorator(func):
    def wrapper():
        print(name.upper())
        func()
    return wrapper





@decorator
def hello():
    print('Привет',name)
hello()