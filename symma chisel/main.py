chislo1 = int(input('Введите трехзначное число: '))
if 100<=chislo1<=999:
    a = int(str(chislo1)[0])*int(str(chislo1)[1])*int(str(chislo1)[2])
    sum=int(str(chislo1)[0])+int(str(chislo1)[1])+int(str(chislo1)[2])
    print('Произведение цифр в числе равно:',a)
    print('Сумма цифр в числе равна:',sum)
else:
    print('Число не трехзначное')