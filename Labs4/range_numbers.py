a = int(input("Введите начало: "))
b = int(input("Введите конец: "))

if a < b:
    current = a
    while current <= b:
        print(current)
        current += 1
elif a > b:
    current = a
    while current >= b:
        print(current)
        current -= 1
else:
    print(a)
