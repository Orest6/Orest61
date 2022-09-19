#Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
messages = list()
n = int(input('text v is: '))
for i in range(n):
    message = input('Введите строку'+str(i+1)+":")
    messages.append(message +"\n")
with open('datafile.txt','a') as data:
    for message in messages:
        data.write(message)
print('Сообщения,введенные пользователем')
with open('datafile.txt','r') as data:
    for message in data:
        print(message,end='')