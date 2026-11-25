"""Лабораторная работа 10. Чтение таблицы из текстового файла и вариант 14."""


def read_matrix(path):
    """Прочитать матрицу из файла в UTF-8.

    Формат: первая строка — «строки столбцы» (положительные целые), далее
    ровно столько строк по столько целых чисел. Пустые и лишние строки —
    ошибка; один перевод строки после последней строки допустим.

    Ошибки формата -> ValueError (с номером строки, если применимо).
    Нет файла -> FileNotFoundError, ошибки доступа -> OSError,
    неверная кодировка -> UnicodeDecodeError (подкласс ValueError/UnicodeError);
    эти исключения обрабатывает основная программа.
    Файл открывается только для чтения.
    """
    with open(path, "r", encoding="utf-8", newline="") as file:
        text = file.read()
    lines = text.splitlines()
    if not lines:
        raise ValueError("Файл пустой")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось два числа — строки и столбцы")
    try:
        rows, columns = int(header[0]), int(header[1])
    except ValueError:
        raise ValueError("Строка 1: размеры должны быть целыми числами")
    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: размеры должны быть больше нуля")

    data_lines = lines[1:]
    if len(data_lines) < rows:
        raise ValueError(
            f"Ожидалось строк данных: {rows}, найдено: {len(data_lines)}"
        )
    if len(data_lines) > rows:
        raise ValueError(
            f"Строка {rows + 2}: лишняя строка после {rows} строк данных"
        )

    matrix = []
    for offset, line in enumerate(data_lines):
        number = offset + 2
        parts = line.split()
        if len(parts) != columns:
            raise ValueError(
                f"Строка {number}: ожидалось {columns} чисел, найдено {len(parts)}"
            )
        try:
            matrix.append([int(part) for part in parts])
        except ValueError:
            raise ValueError(f"Строка {number}: значения должны быть целыми числами")
    return matrix


def selected_sum(matrix):
    """Вариант 14: сумма положительных элементов с нечётным индексом столбца.

    Индексы с нуля. Если подходящих элементов нет — 0. Матрицу не меняет.
    """
    total = 0
    for row in matrix:
        for column, value in enumerate(row):
            if column % 2 == 1 and value > 0:
                total += value
    return total
