#В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить количество символов и слов в ней.
with open('datafile.txt','r',encoding  = 'utf-8') as f: #посчитали кол-во символов строке
    list1 = f.readlines()
    print(list1)
    for i in list1:
        print('Количество символов в строке: ',len(i.replace('\n',''))) #считаем кол-во строк в файле
with open('datafile.txt', 'r',encoding  = 'utf-8') as f:
    list1 = f.readlines()
    print('Количество строк в файле: ',len(list1))
with open('datafile.txt','r',encoding = 'utf-8') as f: #считаем кол-во слов в файле
    list1 = f.readlines()
    words = 0
    for i in list1:
        words +=len(i.split())
    print('Количество слов в файле: ',words)