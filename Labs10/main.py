"""Лабораторная работа 10: чтение matrix.txt и запись report.txt (вариант 14)."""
from pathlib import Path

from files_lab import read_matrix, selected_sum
from table import column_sums, row_sums


def read_positive_integer():
    """Повторять ввод, пока не получено целое число больше нуля."""
    while True:
        text = input("Введите целое число больше нуля: ")
        try:
            value = int(text)
        except ValueError:
            print("Это не целое число")
            continue
        if value <= 0:
            print("Число должно быть больше нуля")
            continue
        return value


def build_report(matrix):
    return (
        "Суммы строк: " + " ".join(map(str, row_sums(matrix))) + "\n"
        "Суммы столбцов: " + " ".join(map(str, column_sums(matrix))) + "\n"
        f"Результат варианта: {selected_sum(matrix)}\n"
    )


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "matrix.txt"
    target = folder / "report.txt"
    try:
        # Сначала читаем и проверяем ВЕСЬ вход, отчёт ещё не тронут.
        matrix = read_matrix(source)
        report = build_report(matrix)
        # Только теперь открываем отчёт для записи.
        with open(target, "w", encoding="utf-8") as file:
            file.write(report)
    except FileNotFoundError:
        print(f"Файл не найден: {source.name}")
    except UnicodeError:
        print("Неверная кодировка входного файла (нужен UTF-8)")
    except ValueError as error:
        print(f"Ошибка формата: {error}")
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
    else:
        print(report, end="")
        print(f"Отчёт сохранён: {target.name}")


if __name__ == "__main__":
    main()
