"""Чтение и запись JSON (без консольных диалогов)."""
import json
import os

from logic import validate_records


def load_records(path):
    """Прочитать и проверить список записей из JSON-файла (UTF-8).

    Исключения: FileNotFoundError (нет файла), OSError (доступ),
    UnicodeDecodeError (кодировка), json.JSONDecodeError (синтаксис),
    ValueError (структура). Файл не изменяется.
    """
    with open(path, "r", encoding="utf-8") as file:
        records = json.load(file)
    validate_records(records)
    return records


def save_records(path, records):
    """Записать список в JSON (UTF-8).

    Данные сначала сериализуются и пишутся во временный файл рядом, затем
    заменяют целевой: при ошибке прежний файл остаётся нетронутым.
    Ошибки записи -> OSError (или TypeError/ValueError при неверных данных).
    """
    text = json.dumps(records, ensure_ascii=False, indent=2) + "\n"
    temp_path = str(path) + ".tmp"
    try:
        with open(temp_path, "w", encoding="utf-8") as file:
            file.write(text)
        os.replace(temp_path, path)
    except BaseException:
        try:
            os.remove(temp_path)
        except OSError:
            pass
        raise
