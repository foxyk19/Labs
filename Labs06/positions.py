numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    biggest = max(numbers)

    indexes = []
    for index, number in enumerate(numbers):
        if number == biggest:
            indexes.append(index)

    print(indexes)
