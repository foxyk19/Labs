"""Лабораторная работа 9. Функции для работы с таблицами (вариант 14).

Все функции работают без ввода и вывода и не изменяют переданную матрицу.
"""


def row_sums(matrix):
    """Вернуть список сумм строк. Для [] вернуть []."""
    return [sum(row) for row in matrix]


def column_sums(matrix):
    """Вернуть список сумм столбцов. Для [] вернуть [].

    Непустая матрица прямоугольная и имеет хотя бы один столбец.
    """
    if not matrix:
        return []
    columns = len(matrix[0])
    sums = [0] * columns
    for row in matrix:
        for index, value in enumerate(row):
            sums[index] += value
    return sums


def diagonal_pattern(size):
    """Квадратная таблица size x size: диагональ 0, выше 1, ниже 2."""
    result = []
    for row in range(size):
        new_row = []
        for column in range(size):
            if row == column:
                new_row.append(0)
            elif row < column:
                new_row.append(1)
            else:
                new_row.append(2)
        result.append(new_row)
    return result


def transform(matrix):
    """Вариант 14: элементы от -2 до 3 включительно возвести в квадрат.

    Возвращает новую матрицу той же формы; исходная не меняется.
    Остальные элементы сохраняются. Для [] результат [].
    """
    return [
        [value ** 2 if -2 <= value <= 3 else value for value in row]
        for row in matrix
    ]
