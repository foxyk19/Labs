"""Лабораторная работа 9: ввод таблицы, суммы, узор, преобразование (вариант 14)."""
from table import column_sums, diagonal_pattern, row_sums, transform


def read_int(prompt, minimum=None):
    """Повторять ввод, пока не получено целое (и не меньше minimum)."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if minimum is not None and value < minimum:
            print(f"Число должно быть не меньше {minimum}")
            continue
        return value


def read_row(prompt, columns):
    """Прочитать строку ровно из columns целых чисел."""
    while True:
        try:
            row = [int(part) for part in input(prompt).split()]
        except ValueError:
            print("Все значения должны быть целыми числами")
            continue
        if len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            continue
        return row


def read_matrix():
    rows = read_int("Количество строк: ", 1)
    columns = read_int("Количество столбцов: ", 1)
    return [read_row(f"Строка {i + 1}: ", columns) for i in range(rows)]


def print_table(matrix):
    for row in matrix:
        print(*row)


def main():
    matrix = read_matrix()
    print("Суммы строк:", *row_sums(matrix))
    print("Суммы столбцов:", *column_sums(matrix))

    print("Исходная таблица:")
    print_table(matrix)
    print("После преобразования (вариант 14):")
    print_table(transform(matrix))

    size = read_int("Размер диагонального узора: ", 1)
    print_table(diagonal_pattern(size))


if __name__ == "__main__":
    main()
