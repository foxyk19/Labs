attempts = 0

while True:
    number = int(input("Введите положительное число: "))
    if number > 0:
        break
    attempts += 1

print("Квадрат:", number * number)
print("Отклонённых попыток:", attempts)
