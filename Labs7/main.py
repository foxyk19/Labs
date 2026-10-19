from functions import average, normalize_text, select_numbers, sum_digits


def main():
    number = int(input("Целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    numbers = []
    for part in input("Целые числа через пробел: ").split():
        numbers.append(int(part))

    avg = average(numbers)
    if avg is None:
        print("Нет данных")
    else:
        print(f"Среднее: {avg:.2f}")

    text = input("Текст: ")
    print(f"Нормализованный текст: {normalize_text(text)}")

    threshold = int(input("Порог (целое неотрицательное): "))
    print(f"Отобранные числа: {select_numbers(numbers, threshold)}")


if __name__ == "__main__":
    main()
