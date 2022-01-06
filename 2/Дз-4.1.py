import math
a = input()
a = [int(i) for i in a.split()]
n = 0
for index in range(0,len(a),2):
    S = a[index] * a[index+1] / 2
    c = math.sqrt(a[index]**2 + a[index+1]**2)
    n += 1
    print(f'Треугольник {n} с катетами {a[index]} и {a[index+1]} имеет площадь {S} и гипотенузу {c}')
    