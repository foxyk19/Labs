import builtins
import io
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

import main
from files_lab import read_matrix, selected_sum


def write(directory, text, name="matrix.txt"):
    path = Path(directory) / name
    path.write_text(text, encoding="utf-8", newline="")
    return path


def expect_value_error(path, *fragments):
    try:
        read_matrix(path)
    except ValueError as error:
        for fragment in fragments:
            assert fragment in str(error), (fragment, str(error))
    else:
        assert False, "Ошибка не обнаружена"


with TemporaryDirectory() as directory:
    # пример из задания
    assert read_matrix(write(directory, "1 2\n7 -1\n")) == [[7, -1]]
    # матрица 1x1
    assert read_matrix(write(directory, "1 1\n0\n")) == [[0]]
    # без завершающего перевода строки
    assert read_matrix(write(directory, "1 1\n5")) == [[5]]
    # файл из задания
    assert read_matrix(write(directory, "2 3\n1 -2 3\n4 0 -6\n")) == [
        [1, -2, 3],
        [4, 0, -6],
    ]

    # ошибки формата
    expect_value_error(write(directory, ""))
    expect_value_error(write(directory, "0 3\n"))
    expect_value_error(write(directory, "2\n1 2\n"))
    expect_value_error(write(directory, "a b\n"))
    expect_value_error(write(directory, "1 2\n1\n"), "Строка 2")
    expect_value_error(write(directory, "1 2\n1 x\n"), "Строка 2")
    expect_value_error(write(directory, "1 1\n0\n1\n"))
    expect_value_error(write(directory, "1 1\n0\n\n"))  # лишняя пустая строка
    expect_value_error(write(directory, "2 1\n0\n"))  # не хватает строк
    expect_value_error(write(directory, "1 1\n\n"))  # пустая строка вместо данных

    # отсутствующий путь
    try:
        read_matrix(Path(directory) / "net_takogo.txt")
    except FileNotFoundError:
        pass
    else:
        assert False, "Ошибка не обнаружена"

# Вариант 14
assert selected_sum([[1, -2, 3], [4, 0, -6]]) == 0  # ответ из таблицы
assert selected_sum([[1, 2, 3], [4, 5, 6]]) == 7  # 2 + 5
assert selected_sum([[1, 2, 3, 4]]) == 6  # столбцы 1 и 3
assert selected_sum([[9]]) == 0  # 1x1: нет нечётного столбца
assert selected_sum([[0, 0], [0, -1]]) == 0
m = [[1, 2], [3, 4]]
selected_sum(m)
assert m == [[1, 2], [3, 4]]


# read_positive_integer: abc, 0, -2, 3
inputs = iter(["abc", "0", "-2", "3"])
original_input = builtins.input
builtins.input = lambda prompt="": next(inputs)
buffer = io.StringIO()
try:
    with redirect_stdout(buffer):
        value = main.read_positive_integer()
finally:
    builtins.input = original_input
assert value == 3
output = buffer.getvalue().splitlines()
assert output == [
    "Это не целое число",
    "Число должно быть больше нуля",
    "Число должно быть больше нуля",
], output

# отчёт
assert main.build_report([[1, -2, 3], [4, 0, -6]]) == (
    "Суммы строк: 2 -2\nСуммы столбцов: 5 -2 -3\nРезультат варианта: 0\n"
)

print("Все проверки лабораторной 10 пройдены")
