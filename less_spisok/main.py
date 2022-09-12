#Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
#Освободившиеся в конце массива элементы заполнить нулями.
import random

listA = [random.randint(1, 25) for i in range(10)]
a = int(input('Введите начало: '))
b = int(input('Введите конец: '))
cnt = 0
for i in range(a, b + 1):
    if i in listA:
        listA.remove(i)
        cnt += 1
        listA.append(0)
print(listA)
