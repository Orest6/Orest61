import random
n = random.randint(0,1234567890)
print(n)
summ = 0
for i in str(n):
    summ+=int(i)
print(summ)