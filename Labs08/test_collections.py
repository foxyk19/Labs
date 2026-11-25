from collections_lab import (
    SAMPLE_RECORDS,
    STUDY_RECORDS,
    all_topics,
    build_record_demo,
    common_topics,
    titles_in_category,
    totals_by_category,
    word_counts,
)

# Задание 1. Частоты слов
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}
assert word_counts("  a   A, b;  ") == {"a": 2, "b": 1}

# Задание 2. Темы
assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]
assert common_topics([], ["sql", "git"]) == []
assert all_topics([], ["sql", "git", "sql"]) == ["git", "sql"]
assert common_topics(["a"], []) == []
assert all_topics([], []) == []

# Задание 3. Запись и пара
record, title, hours = build_record_demo()
assert record == {"title": "Python", "hours": 6, "completed": False}
assert title == "Python"
assert hours == 6

# Индивидуальный вариант: общий набор
assert totals_by_category(SAMPLE_RECORDS) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(SAMPLE_RECORDS, "основное") == ["A", "C"]
assert titles_in_category(SAMPLE_RECORDS, "нет") == []
assert totals_by_category([]) == {}
assert titles_in_category([], "основное") == []

# Индивидуальный вариант: собственный набор (учебные занятия, часы)
assert totals_by_category(STUDY_RECORDS) == {"лекция": 5, "практика": 7, "семинар": 1}
assert titles_in_category(STUDY_RECORDS, "лекция") == [
    "Лекция по спискам",
    "Лекция по словарям",
    "Лекция по циклам",
]
assert titles_in_category(STUDY_RECORDS, "семинар") == ["Семинар по тестам"]
assert titles_in_category(STUDY_RECORDS, "экзамен") == []

# Исходные записи после вызовов не изменились
for records in [SAMPLE_RECORDS, STUDY_RECORDS]:
    saved = [record.copy() for record in records]
    totals_by_category(records)
    titles_in_category(records, "основное")
    assert records == saved

print("Все проверки пройдены")
