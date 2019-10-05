# Задание 1, вариант 2
import math
x, y = (float(i) for i in input().split())
try:
    d = (2*math.cos(x-math.pi/6))/(1/2+(math.sin(y))**2) + abs(y-x)/3
except ZeroDivisionError:
    print('Деление на ноль!')
print(d)

# Задание 2, 2 вариант
x, y = (float(i) for i in input().split())
if x < y:
    h = math.atan(x+abs(y))
elif x > y:
    h = math.atan(abs(x)+y)
elif x == y:
    h = (x+y)**2
print(h)
