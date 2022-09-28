#В зависимости от выбора пользователя, вычислить площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.
import math
choose= input('choose ')
sqr = int(input())
def square_circle(r,choose):
 return r
r = math.pi*sqr**2
def triangle(d,choose):
 return d
d=((sqr**2)*math.sqrt(3))/4
def square(k,choose):
    return k
k = sqr**2
if choose=='circle':
 print(r)
elif choose=='triangle':
 print(d)
elif choose == 'square':
    print(k)