# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = ['orange', 'apple', 'bannana', 'kiwi', 'watermelon', 'lemon', 'pineapple']
b = ['bannana', 'apple', 'orange', 'kiwi', 'strawberry', 'blueberries', 'pineapple']
aa = a.copy()
for fruit in aa:
    if fruit in b:
        a.remove(fruit)
print(aa)
print(a)