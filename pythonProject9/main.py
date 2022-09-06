chislo1 = int(input('Введите число: '))
factorial = 1
for i in range(1, chislo1+1):
    factorial*=i
print('Факториал числа',chislo1,'равен',factorial)