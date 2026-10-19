numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    total = sum(numbers)
    average = total / len(numbers)

    print(f"Количество: {len(numbers)}")
    print(f"Сумма: {total}")
    print(f"Минимум: {min(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Среднее: {average:.2f}")
