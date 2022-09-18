#Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа
listA = [4,9,5,7,3]
cnt = 0
for i in listA:
    listA.remove(i)
    cnt += i
listA = tuple(listA)
print(listA)