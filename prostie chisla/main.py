n = int(input())
for i in range(n):
    summ = 0
    for k in range(1,i+1):
        if i%k == 0:
            summ +=k
    if i+1 == summ:
        print(str(i)+' - простое')