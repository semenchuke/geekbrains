# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

a = ['apple', 'bannana', 'kiwi', 'watermelon', 'lemon', 'pineapple']
i = 1
for fruit in a:
    String = ' {}'.format(fruit)
    print(str(i) + '.' '{:>12}'.format(String))
    i += 1

