# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

i = int(input("Are you already 18 years old? Please write down your age... "))
if 35 >= i >= 18:
    print("Access confirmed")
elif 0 < i < 17:
    print("You are to young")
elif 35 < i :
    print("You are to old")
else:
    print("wrong number")