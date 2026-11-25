"""Лабораторная работа 12 (вариант 14: план мероприятий).

Логика без ввода/вывода и без файлов. Запись:
{"id": int, "title": str, "category": str, "amount": int, "completed": bool},
где amount — количество участников, completed — мероприятие проведено.

Состояние не хранится в глобальных переменных: список записей передаётся
в функции явно.
"""

REQUIRED_KEYS = ("id", "title", "category", "amount", "completed")


def _is_int(value):
    """Строгое целое: bool не подходит."""
    return type(value) is int


def validate_records(records):
    """Проверить весь набор записей; при нарушении — ValueError.

    Ничего не изменяет и ничего не возвращает. Дополнительные ключи допустимы.
    """
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком")
    seen = set()
    for index, record in enumerate(records, start=1):
        where = f"Запись {index}"
        if not isinstance(record, dict):
            raise ValueError(f"{where}: ожидался объект")
        for key in REQUIRED_KEYS:
            if key not in record:
                raise ValueError(f"{where}: нет ключа '{key}'")
        if not _is_int(record["id"]) or record["id"] <= 0:
            raise ValueError(f"{where}: 'id' должен быть положительным целым")
        if record["id"] in seen:
            raise ValueError(f"{where}: повторяющийся id {record['id']}")
        seen.add(record["id"])
        for key in ("title", "category"):
            if not isinstance(record[key], str) or not record[key].strip():
                raise ValueError(f"{where}: '{key}' должна быть непустой строкой")
        if not _is_int(record["amount"]) or record["amount"] < 0:
            raise ValueError(f"{where}: 'amount' должно быть целым не меньше 0")
        if type(record["completed"]) is not bool:
            raise ValueError(f"{where}: 'completed' должно быть true или false")


def next_id(records):
    """max(id) + 1; для пустого списка — 1. Список не меняет."""
    return max((record["id"] for record in records), default=0) + 1


def add_record(records, title, category, amount):
    """Добавить запись В КОНЕЦ списка `records` (список изменяется).

    Пробелы по краям названия и категории убираются; статус — False.
    Возвращает добавленную запись. Некорректные данные -> ValueError,
    список при этом не меняется.
    """
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название не должно быть пустым")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Категория не должна быть пустой")
    if not _is_int(amount) or amount < 0:
        raise ValueError("Количество должно быть целым числом не меньше 0")
    record = {
        "id": next_id(records),
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    """Записи, в названии которых есть подстрока `query` (без учёта регистра).

    Возвращает новый список в порядке исходного списка; `records` не меняет.
    Пустой запрос (после strip) -> ValueError.
    """
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Поисковый запрос не должен быть пустым")
    needle = query.strip().casefold()
    return [r for r in records if needle in r["title"].casefold()]


def set_completed(records, record_id, completed):
    """Установить статус записи с данным id (список изменяется).

    Возвращает True при успехе и False, если запись не найдена
    (данные при этом не меняются).
    """
    for record in records:
        if record["id"] == record_id:
            record["completed"] = bool(completed)
            return True
    return False


def delete_record(records, record_id):
    """Удалить запись по id (список изменяется, остальные id сохраняются).

    Возвращает True при успехе и False, если запись не найдена.
    """
    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def sorted_records(records):
    """Новый список записей по возрастанию id; `records` не меняет."""
    return sorted(records, key=lambda record: record["id"])


def statistics(records):
    """Статистика по текущему списку (данные не меняются).

    Возвращает словарь: total, done, not_done, amount_total и by_category —
    словарь {категория: сумма amount}, ключи по алфавиту. Категории
    сравниваются точно после удаления краевых пробелов.
    """
    by_category = {}
    amount_total = 0
    done = 0
    for record in records:
        category = record["category"].strip()
        by_category[category] = by_category.get(category, 0) + record["amount"]
        amount_total += record["amount"]
        if record["completed"]:
            done += 1
    return {
        "total": len(records),
        "done": done,
        "not_done": len(records) - done,
        "amount_total": amount_total,
        "by_category": dict(sorted(by_category.items())),
    }
