#Вывести на экран столько элементов ряда Фибоначчи, сколько указал пользователь.
#Например, если на ввод поступило число 6, то вывод должен содержать шесть первых чисел ряда Фибоначчи: 1 2 3 5 8 13.
f1 = 1
f2 = 1
n = int(input('Введите количество чисел в последовательности: '))
print(f1, f2, end=' ')
for i in range(2,n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
