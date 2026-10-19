# Вариант 1: учебные занятия, поле amount — часы.

# Общий набор для проверки
SAMPLE_RECORDS = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]

# Собственный набор варианта: шесть записей, три категории, "лекция" и "практика" повторяются
STUDY_RECORDS = [
    {"title": "Лекция по спискам", "category": "лекция", "amount": 2},
    {"title": "Практика по функциям", "category": "практика", "amount": 3},
    {"title": "Лекция по словарям", "category": "лекция", "amount": 2},
    {"title": "Семинар по тестам", "category": "семинар", "amount": 1},
    {"title": "Практика по строкам", "category": "практика", "amount": 4},
    {"title": "Лекция по циклам", "category": "лекция", "amount": 1},
]


# --- Задание 1. Частоты слов ---

def word_counts(text):
    """Вернуть словарь «слово -> количество»."""
    counts = {}
    for word in text.lower().split():
        clean = word.strip(".,!?;:")
        if clean == "":
            continue
        counts[clean] = counts.get(clean, 0) + 1
    return counts


def print_word_counts(counts):
    """Вывести пары «слово: количество» по алфавиту."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


# --- Задание 2. Учебные интересы ---

def common_topics(first, second):
    """Вернуть отсортированный список общих тем."""
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Вернуть отсортированный список всех уникальных тем."""
    return sorted(set(first) | set(second))


# --- Задание 3. Запись и пара ---

def build_record_demo():
    """Создать запись, изменить её и распаковать пару (title, hours)."""
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6
    record["completed"] = False

    pair = (record["title"], record["hours"])
    title, hours = pair
    return record, title, hours


# --- Индивидуальный вариант ---

def totals_by_category(records):
    """Вернуть словарь «категория -> сумма amount»."""
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    """Вернуть названия записей категории в исходном порядке."""
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles


def main():
    text = input("Текст для подсчёта слов: ")
    print_word_counts(word_counts(text))

    first = input("Темы первого студента (через пробел): ").split()
    second = input("Темы второго студента (через пробел): ").split()
    print(f"Общие темы: {common_topics(first, second)}")
    print(f"Все темы: {all_topics(first, second)}")

    record, title, hours = build_record_demo()
    print(f"Запись: {record}")
    print(f"Пара: {title}, {hours}")

    totals = totals_by_category(STUDY_RECORDS)
    print("Часы по категориям:")
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")

    wanted = input("Категория для поиска: ")
    print(titles_in_category(STUDY_RECORDS, wanted))


if __name__ == "__main__":
    main()
