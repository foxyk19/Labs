"""Лабораторная работа 12: консольное меню «План мероприятий» (вариант 14).

Запуск: python main.py [путь_к_json]
По умолчанию используется data.json из папки проекта.
"""
import json
import sys
from pathlib import Path

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    sorted_records,
    statistics,
)
from storage import load_records, save_records

UNIT = "участников"
DONE = "проведено"
NOT_DONE = "не проведено"

MENU = """
=== План мероприятий ===
1. Показать записи
2. Добавить запись
3. Найти записи
4. Изменить статус
5. Удалить запись
6. Показать статистику
7. Сохранить данные
8. Выйти"""


def read_nonempty(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Значение не должно быть пустым")


def read_amount(prompt):
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if value < 0:
            print("Число не должно быть отрицательным")
            continue
        return value


def read_id(prompt):
    """ID записи: целое число; возвращает None, если ввод не число."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("ID должен быть целым числом")
        return None


def format_record(record):
    status = DONE if record["completed"] else NOT_DONE
    return (f"ID {record['id']}: {record['title']} | {record['category']} | "
            f"{UNIT}: {record['amount']} | {status}")


def show_records(records):
    if not records:
        print("Нет записей")
        return
    for record in sorted_records(records):
        print(format_record(record))


def cmd_add(records):
    title = read_nonempty("Название: ")
    category = read_nonempty("Категория: ")
    amount = read_amount(f"Количество {UNIT}: ")
    record = add_record(records, title, category, amount)
    print(f"Добавлена запись с ID {record['id']}")


def cmd_find(records):
    query = input("Подстрока названия: ")
    try:
        found = find_records(records, query)
    except ValueError as error:
        print(error)
        return
    if not found:
        print("Ничего не найдено")
        return
    for record in found:
        print(format_record(record))


def cmd_status(records):
    record_id = read_id("ID записи: ")
    if record_id is None:
        return
    if not any(r["id"] == record_id for r in records):
        print("Запись с таким ID не найдена")
        return
    while True:
        answer = input(f"Новый статус (1 — {DONE}, 2 — {NOT_DONE}): ").strip()
        if answer in ("1", "2"):
            break
        print("Введите 1 или 2")
    set_completed(records, record_id, answer == "1")
    print("Статус изменён")


def cmd_delete(records):
    record_id = read_id("ID записи: ")
    if record_id is None:
        return
    if not any(r["id"] == record_id for r in records):
        print("Запись с таким ID не найдена")
        return
    if input("Удалить? Введите «да» для подтверждения: ").strip().lower() != "да":
        print("Удаление отменено")
        return
    delete_record(records, record_id)
    print("Запись удалена")


def cmd_statistics(records):
    stats = statistics(records)
    print(f"Всего записей: {stats['total']}")
    print(f"{DONE.capitalize()}: {stats['done']}")
    print(f"{NOT_DONE.capitalize()}: {stats['not_done']}")
    print(f"Сумма ({UNIT}): {stats['amount_total']}")
    print("По категориям:")
    if not stats["by_category"]:
        print("  нет данных")
    for category, total in stats["by_category"].items():
        print(f"  {category}: {total}")


def try_save(path, records):
    """Сохранить данные; True только при успешной записи."""
    try:
        save_records(path, records)
    except (OSError, TypeError, ValueError) as error:
        print(f"Не удалось сохранить данные: {error}")
        return False
    print("Данные сохранены")
    return True


def cmd_exit(path, records):
    """Вернуть True, если программу можно завершать."""
    while True:
        answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
        if answer == "да":
            return try_save(path, records)  # при ошибке остаёмся в меню
        if answer == "нет":
            return True
        print("Ответьте «да» или «нет»")


def load_at_start(path):
    """Загрузить данные. Возвращает список или None, если запуск невозможен."""
    try:
        records = load_records(path)
    except FileNotFoundError:
        print(f"Файл {path.name} не найден — начинаем с пустого списка")
        return []
    except UnicodeError:
        print("Ошибка: файл не в кодировке UTF-8. Файл не изменён.")
    except json.JSONDecodeError as error:
        print(f"Ошибка: повреждённый JSON ({error}). Файл не изменён.")
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}. Файл не изменён.")
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
    else:
        print(f"Загружено записей: {len(records)}")
        return records
    return None


def main():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    else:
        path = Path(__file__).resolve().parent / "data.json"

    records = load_at_start(path)
    if records is None:
        return 1

    commands = {
        "1": show_records,
        "2": cmd_add,
        "3": cmd_find,
        "4": cmd_status,
        "5": cmd_delete,
        "6": cmd_statistics,
    }
    while True:
        print(MENU)
        choice = input("Команда: ").strip()
        if choice in commands:
            commands[choice](records)
        elif choice == "7":
            try_save(path, records)
        elif choice == "8":
            if cmd_exit(path, records):
                break
        else:
            print("Неизвестная команда")
    return 0


if __name__ == "__main__":
    sys.exit(main())
