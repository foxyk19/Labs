# Номер варианта (1-15). Поменяйте на свой.
VARIANT = 1

numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

selected = []
for number in numbers:
    match = False

    if VARIANT == 1:
        match = number % 2 == 0
    elif VARIANT == 2:
        match = number < 0
    elif VARIANT == 3:
        match = abs(number) > 5
    elif VARIANT == 4:
        match = number % 2 != 0
    elif VARIANT == 5:
        match = number > 0
    elif VARIANT == 6:
        match = number % 3 == 0
    elif VARIANT == 7:
        match = number % 3 != 0
    elif VARIANT == 8:
        match = 10 <= number <= 20
    elif VARIANT == 9:
        match = number != 0
    elif VARIANT == 10:
        match = number >= 10
    elif VARIANT == 11:
        match = abs(number) <= 3
    elif VARIANT == 12:
        match = number > 0 and number % 2 == 0
    elif VARIANT == 13:
        match = number < 0 and number % 2 != 0
    elif VARIANT == 14:
        match = number % 5 == 0
    elif VARIANT == 15:
        match = abs(number) % 10 == 2

    if match:
        selected.append(number)

# sorted() возвращает новый список, selected остаётся в исходном порядке
sorted_copy = sorted(selected)

print(f"Выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted_copy}")
