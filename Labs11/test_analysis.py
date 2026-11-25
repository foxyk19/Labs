import json
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import (
    completion_counts,
    dump_json,
    leader_tasks,
    load_todos,
    select_tasks,
    top_users,
    validate_todos,
)

TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]


def expect_value_error(data):
    try:
        validate_todos(data)
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"


# --- учебный набор ---
validate_todos(TODOS)
assert completion_counts(TODOS) == {5: 2, 10: 2}
assert top_users({5: 2, 10: 2}) == [5, 10]
assert [t["id"] for t in leader_tasks(TODOS, [5, 10])] == [1, 3, 4, 5]

# --- пустой набор и набор без выполненных ---
assert completion_counts([]) == {}
assert top_users({}) == []
assert leader_tasks([], []) == []
only_open = [
    {"id": 1, "userId": 1, "title": "А", "completed": False},
    {"id": 2, "userId": 2, "title": "Б", "completed": False},
]
assert completion_counts(only_open) == {1: 0, 2: 0}
assert top_users(completion_counts(only_open)) == []
assert leader_tasks(only_open, top_users(completion_counts(only_open))) == []

# --- единственный лидер / несколько лидеров ---
mixed = TODOS + [{"id": 6, "userId": 10, "title": "Ещё", "completed": True}]
assert completion_counts(mixed) == {5: 2, 10: 3}
assert top_users(completion_counts(mixed)) == [10]
assert top_users({3: 1, 1: 1, 2: 0}) == [1, 3]  # отсортировано
assert top_users({1: 0, 2: 0}) == []

# пользователь с нулём выполненных присутствует в словаре
zero = TODOS + [{"id": 7, "userId": 7, "title": "Пока нет", "completed": False}]
assert completion_counts(zero) == {5: 2, 10: 2, 7: 0}

# --- вариант 14: незавершённые, длина названия >= порога ---
def ids(items):
    return [t["id"] for t in items]


assert ids(select_tasks(TODOS, 5, 5)) == [2]  # пример из таблицы
assert ids(select_tasks(TODOS, 5, 6)) == []  # граница: длина 5 < 6
assert ids(select_tasks(TODOS, 5, 5)) == [2]  # граница: длина 5 == 5
assert ids(select_tasks(TODOS, 5, 0)) == [2]  # порог 0
assert select_tasks(TODOS, 999, 0) == []  # неизвестный пользователь
assert select_tasks(TODOS, 10, 0) == []  # у пользователя 10 нет незавершённых
assert select_tasks([], 5, 0) == []
# порядок сохраняется
many = [
    {"id": 9, "userId": 1, "title": "abcdef", "completed": False},
    {"id": 3, "userId": 1, "title": "abcdefg", "completed": False},
    {"id": 4, "userId": 1, "title": "abc", "completed": False},
]
assert ids(select_tasks(many, 1, 4)) == [9, 3]
# параметр обязателен и проверяется
for bad in (None, -1, "5", True, 2.5):
    try:
        select_tasks(TODOS, 5, bad)
    except ValueError:
        pass
    else:
        assert False, f"Порог {bad!r} должен отклоняться"
# исходные записи не изменяются
snapshot = json.loads(json.dumps(TODOS))
result = select_tasks(TODOS, 5, 5)
result[0]["title"] = "изменено"
assert TODOS == snapshot

# --- ошибки структуры ---
expect_value_error({"id": 1})  # объект вместо списка
expect_value_error([TODOS[0], dict(TODOS[1], id=1)])  # повторный id
expect_value_error([{"id": 1, "title": "x", "completed": True}])  # нет userId
expect_value_error([dict(TODOS[0], completed="false")])
expect_value_error([dict(TODOS[0], id=True)])
expect_value_error([dict(TODOS[0], userId=True)])
expect_value_error([dict(TODOS[0], id=0)])
expect_value_error([dict(TODOS[0], title="   ")])
expect_value_error(["не объект"])
validate_todos([dict(TODOS[0], extra="допустимо")])  # доп. ключи разрешены

# --- запись и повторное чтение ---
with TemporaryDirectory() as directory:
    path = Path(directory) / "selected.json"
    selected = select_tasks(TODOS, 5, 5)
    dump_json(path, selected)
    assert json.loads(path.read_text(encoding="utf-8")) == selected

    todos_path = Path(directory) / "todos.json"
    dump_json(todos_path, TODOS)
    assert load_todos(todos_path) == TODOS

    # некорректный JSON и неверная кодировка
    bad_json = Path(directory) / "bad.json"
    bad_json.write_text("{'a': None}", encoding="utf-8")
    try:
        load_todos(bad_json)
    except json.JSONDecodeError:
        pass
    else:
        assert False
    bad_enc = Path(directory) / "enc.json"
    bad_enc.write_bytes(b"\xff\xfe\x00")
    try:
        load_todos(bad_enc)
    except UnicodeError:
        pass
    else:
        assert False

print("Все проверки лабораторной 11 пройдены")
