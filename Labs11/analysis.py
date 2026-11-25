"""Лабораторная работа 11. Проверка и анализ списка задач (вариант 14).

Модуль не выполняет сетевых запросов и не использует ввод/вывод консоли.
"""
import json


def _is_int(value):
    """Строгое целое: bool не подходит."""
    return type(value) is int


def validate_todos(data):
    """Проверить структуру набора задач; при нарушении — ValueError.

    Корень — список; каждая запись — словарь с положительными целыми
    `id` и `userId`, непустой строкой `title` и логическим `completed`.
    `id` уникален. Дополнительные ключи допустимы. Данные не меняются.
    """
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком")
    seen = set()
    for index, record in enumerate(data, start=1):
        where = f"Запись {index}"
        if not isinstance(record, dict):
            raise ValueError(f"{where}: ожидался объект")
        for key in ("id", "userId", "title", "completed"):
            if key not in record:
                raise ValueError(f"{where}: нет ключа '{key}'")
        if not _is_int(record["id"]) or record["id"] <= 0:
            raise ValueError(f"{where}: 'id' должен быть положительным целым")
        if not _is_int(record["userId"]) or record["userId"] <= 0:
            raise ValueError(f"{where}: 'userId' должен быть положительным целым")
        if not isinstance(record["title"], str) or not record["title"].strip():
            raise ValueError(f"{where}: 'title' должен быть непустой строкой")
        if type(record["completed"]) is not bool:
            raise ValueError(f"{where}: 'completed' должен быть true или false")
        if record["id"] in seen:
            raise ValueError(f"{where}: повторяющийся id {record['id']}")
        seen.add(record["id"])


def completion_counts(todos):
    """Словарь {userId: число выполненных задач} для ВСЕХ пользователей набора.

    Пользователи без выполненных задач получают 0. Данные не меняются.
    """
    counts = {}
    for todo in todos:
        user = todo["userId"]
        counts.setdefault(user, 0)
        if todo["completed"]:
            counts[user] += 1
    return counts


def top_users(counts):
    """Отсортированный список userId с максимальным числом выполненных задач.

    Для пустого словаря или максимума 0 возвращает [].
    """
    if not counts:
        return []
    best = max(counts.values())
    if best == 0:
        return []
    return sorted(user for user, value in counts.items() if value == best)


def leader_tasks(todos, leaders):
    """Завершённые задачи пользователей из `leaders` в исходном порядке."""
    leader_set = set(leaders)
    return [
        todo for todo in todos
        if todo["completed"] and todo["userId"] in leader_set
    ]


def select_tasks(todos, user_id, parameter=None):
    """Вариант 14: незавершённые задачи пользователя с длиной названия
    не меньше порога `parameter` (целое неотрицательное).

    Порядок записей сохраняется; для неизвестного пользователя — [].
    Исходные записи не изменяются (возвращаются копии).
    """
    if not _is_int(parameter) or parameter < 0:
        raise ValueError("Порог должен быть целым неотрицательным числом")
    return [
        dict(todo) for todo in todos
        if todo["userId"] == user_id
        and not todo["completed"]
        and len(todo["title"]) >= parameter
    ]


def load_todos(path):
    """Прочитать JSON-файл (UTF-8) и проверить структуру.

    Исключения: FileNotFoundError / OSError (доступ), UnicodeDecodeError
    (кодировка), json.JSONDecodeError (синтаксис), ValueError (структура).
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    validate_todos(data)
    return data


def dump_json(path, data):
    """Записать данные в JSON (UTF-8). Сначала сериализация, потом запись,
    чтобы ошибка сериализации не оставила пустой файл."""
    text = json.dumps(data, ensure_ascii=False, indent=2)
    with open(path, "w", encoding="utf-8") as file:
        file.write(text + "\n")
