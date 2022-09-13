listC = []
stroki = int(input('Введите кол-во строк матрицы: '))
stolbiky = int(input('Введите кол-во столбцов матрицы: '))
for i in range(stroki):
    listC1 = []
    for j in range(stolbiky):
        a = int(input(f'Введите {j}-ый элемент матрицы в строке {i} - '))
        listC1.append(a)
    listC.append(listC1)
maximum = listC[0][0]
for i in listC:
    print(i)
for i in range(0,len(listC)):
    if maximum < listC[i][i]:
        maximum = listC[i][i]
print(maximum)
for i in listC:
    print(i)
q = 0
for i in range(0,len(listC)):
    for g in range(0,len(listC)):
        if g>= i:
            break
        else:
            if listC[i][g]<0:
                q +=1
print('кол-во отрицательных элементов под главной диагональю - ', q)
