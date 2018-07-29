# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
A = []
LenA = int(input('Please, write down here the preferable length of your list... '))
i = 0
while i < LenA:
    B = random.randint(-100, 100)
    A.append(B)
    i += 1
print('The list A itself:', A)
print('And its length is', len(A), 'elements.')
