# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

i = int(input("write a number, please "))
print("начальное чило - ",i)
big = 0
while (i // 10) > 0:
    amax = i % 10
    i = i // 10
    if big < amax:
        big = amax
if big < i:
    big = i
print("самая большая цифра в вашем числе равна = ", big)