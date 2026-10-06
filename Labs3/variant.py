value = int(input("Введите число от 0 до 100: "))

if value < 0 or value > 100:
    print("Ошибка диапазона")
elif value <= 19:
    print("Низкий")
elif value <= 79:
    print("Средний")
else:
    print("Высокий")
