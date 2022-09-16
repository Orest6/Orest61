#Сгенерировать n множеств (нумерацию начать с 1).
#Вывести элементы, которые входят во все множества с номерами, кратными трём, но не входят в первое множество.
import random

dict = {}
for i in range(1,10):
    dict[i] = set(random.randint(1,50) for i in range(10))

listA = []

for i in dict:
    if i%3 == 0:
        listA.append(list(dict[i]))

set1 = set(listA[0])
for i in range(1,len(listA)):
    set1 = set1 & set(listA[i])

print(set1.difference(dict[1]))





