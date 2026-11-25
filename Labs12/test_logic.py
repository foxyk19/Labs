import json

from logic import (
    add_record,
    delete_record,
    find_records,
    next_id,
    set_completed,
    statistics,
    validate_records,
)


def make_record(**changes):
    record = {"id": 1, "title": "Python", "category": "учёба", "amount": 4,
              "completed": False}
    record.update(changes)
    return record


def expect_error(func, *args):
    try:
        func(*args)
    except ValueError:
        return
    assert False, "Ошибка не обнаружена"


# --- пустой список ---
assert statistics([]) == {"total": 0, "done": 0, "not_done": 0,
                          "amount_total": 0, "by_category": {}}
assert find_records([], "x") == []
assert next_id([]) == 1
validate_records([])

# --- добавление: обрезка пробелов, статус, id ---
records = []
first = add_record(records, "  Python  ", " учёба ", 4)
assert first == {"id": 1, "title": "Python", "category": "учёба",
                 "amount": 4, "completed": False}
assert records == [first]

# --- повторяющиеся названия разрешены, id разные ---
second = add_record(records, "Python", "учёба", 2)
assert second["id"] == 2 and first["title"] == second["title"]

# --- сценарий приёмки: количества 4 и 2, вторая завершена ---
assert set_completed(records, 2, True) is True
stats = statistics(records)
assert (stats["total"], stats["done"], stats["not_done"],
        stats["amount_total"]) == (2, 1, 1, 6)

# --- некорректный ввод: список не растёт ---
for bad in (("", "к", 1), ("   ", "к", 1), ("н", "", 1), ("н", "к", -1),
            ("н", "к", True), ("н", "к", "abc"), ("н", "к", 1.5)):
    expect_error(add_record, records, *bad)
assert len(records) == 2

# --- удаление: id не перенумеровываются ---
assert delete_record(records, 1) is True
assert [r["id"] for r in records] == [2]
assert add_record(records, "Новая", "учёба", 1)["id"] == 3
assert delete_record(records, 999) is False
assert len(records) == 2

# --- неизвестный id при смене статуса ---
before = json.loads(json.dumps(records))
assert set_completed(records, 999, True) is False
assert records == before
# явное снятие статуса
assert set_completed(records, 2, False) is True
assert records[0]["completed"] is False

# --- поиск без учёта регистра ---
data = [make_record(id=1, title="Python"), make_record(id=2, title="Java")]
assert find_records(data, "PY") == [data[0]]
assert find_records(data, "py") == [data[0]]
assert find_records(data, "ruby") == []
assert find_records(data, "  jav ") == [data[1]]
expect_error(find_records, data, "")
expect_error(find_records, data, "   ")

# --- статистика по двум категориям, порядок по алфавиту, неизменность ---
data = [
    make_record(id=1, category="учёба", amount=4, completed=True),
    make_record(id=2, category="быт", amount=3),
    make_record(id=3, category=" учёба ", amount=5),
]
snapshot = json.loads(json.dumps(data))
stats = statistics(data)
assert stats == {"total": 3, "done": 1, "not_done": 2, "amount_total": 12,
                 "by_category": {"быт": 3, "учёба": 9}}
assert list(stats["by_category"]) == ["быт", "учёба"]
assert data == snapshot
find_records(data, "py")
assert data == snapshot

# --- строгие типы полей ---
validate_records([make_record()])
validate_records([make_record(extra="допустимо")])
expect_error(validate_records, {"id": 1})  # не список
expect_error(validate_records, ["строка"])  # не словарь
expect_error(validate_records, [make_record(), make_record(title="Другое")])  # повтор id
expect_error(validate_records, [make_record(id=True)])
expect_error(validate_records, [make_record(id=0)])
expect_error(validate_records, [make_record(id="1")])
expect_error(validate_records, [make_record(amount=True)])
expect_error(validate_records, [make_record(amount=-1)])
expect_error(validate_records, [make_record(amount=1.5)])
expect_error(validate_records, [make_record(completed=1)])
expect_error(validate_records, [make_record(completed="false")])
expect_error(validate_records, [make_record(title="  ")])
expect_error(validate_records, [make_record(category=5)])
broken = make_record()
del broken["amount"]
expect_error(validate_records, [broken])

print("Все проверки test_logic пройдены")
