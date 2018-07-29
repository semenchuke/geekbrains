# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

import math
equation = input('Введите линейную функцию в формате y = kx + b: ')
x = int(input('введите аргумент функции... '))
a = equation.split(' ')
print(a)
for i in a:
    if i.rfind('x') != -1:
        k = i[:-1]
        if type(float(k)) == float or type(int(k)) == int:
            if type(float(k)) == float:
                k = float(k)
            else:
                k = int(k)
    try:
        if type(float(i)) == float or type(int(i)) == int:
            if type(float(i)) == float:
                b = float(i)
            else:
                b = int(i)
    except ValueError:
        continue
if a[3] == '+':
    y = k * x + b
else:
    y = k * x - b
print(y)