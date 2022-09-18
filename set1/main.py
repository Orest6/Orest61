dict1 = {'cat':'кошка',
         'dog':'собака',
         'cry':'плакать'}
str = input('Введите слово')
for key,val in dict1.items():
    if str == key:
        print(val)
    elif str == val:
        print(key)
else:
    print('В словаре нет такого слова')
