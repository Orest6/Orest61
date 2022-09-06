c = int(input('Введите пятизначное число'))
max_elem = 0
if c>0 and len(str(c))==5:
    for i in str(c):
        if int(i) > max_elem:
            max_elem = int(i)
    print('Наибольшая цифра:', max_elem)