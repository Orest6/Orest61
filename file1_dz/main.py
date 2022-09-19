#В текстовый файл построчно записаны фамилия и имя каждого учащегося класса и их оценка за контрольную.
#Вывести на экран всех учащихся, чья оценка меньше 3 баллов, и посчитать средний балл по классу.
with open("textfile.txt","r") as f:
    counter = summ = 0
    for line in f:
        counter +=1
        lenght_line = len(line)
        for i in range(lenght_line):
            if line[i].isdigit():
                num = int(line[i])
                summ += num
                if num <3:
                    print('оценка ученика меньше 3: \n', line)
                    break
    sred = summ/counter
    print('Средний балл по классу', sred)