# Номер варианта (1-15). Поменяйте на свой.
VARIANT = 1


def sum_digits(number):
    """Вернуть сумму цифр модуля целого числа."""
    rest = abs(number)
    total = 0
    while rest > 0:
        total += rest % 10
        rest = rest // 10
    return total


def average(numbers):
    """Вернуть среднее списка чисел или None, если список пуст."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Вернуть текст в нижнем регистре с одним пробелом между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вернуть новый список чисел, подходящих под условие варианта."""
    result = []
    for number in numbers:
        match = False

        if VARIANT == 1:
            match = number > threshold
        elif VARIANT == 2:
            match = number < threshold
        elif VARIANT == 3:
            match = abs(number) > threshold
        elif VARIANT == 4:
            match = number >= threshold
        elif VARIANT == 5:
            match = number <= threshold
        elif VARIANT == 6:
            match = number == threshold
        elif VARIANT == 7:
            match = number != threshold
        elif VARIANT == 8:
            match = abs(number) <= threshold
        elif VARIANT == 9:
            match = 0 <= number <= threshold
        elif VARIANT == 10:
            match = -threshold <= number <= 0
        elif VARIANT == 11:
            match = abs(number) == threshold
        elif VARIANT == 12:
            match = number % 2 == 0 and number > threshold
        elif VARIANT == 13:
            match = number % 2 != 0 and number < threshold
        elif VARIANT == 14:
            match = number % (threshold + 1) == 0
        elif VARIANT == 15:
            match = threshold < abs(number) < 2 * threshold

        if match:
            result.append(number)
    return result
