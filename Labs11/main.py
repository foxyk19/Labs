"""Лабораторная работа 11: анализ todos.json (вариант 14)."""
import json
from pathlib import Path

from analysis import (
    completion_counts,
    dump_json,
    leader_tasks,
    load_todos,
    select_tasks,
    top_users,
)


def read_user_id():
    """Положительное целое, повторный ввод при ошибке."""
    while True:
        text = input("Введите userId (положительное целое): ").strip()
        try:
            value = int(text)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if value <= 0:
            print("Число должно быть больше нуля")
            continue
        return value


def read_threshold():
    """Порог длины названия: целое неотрицательное, повторный ввод."""
    while True:
        text = input("Минимальная длина названия (целое >= 0): ").strip()
        try:
            value = int(text)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if value < 0:
            print("Число не должно быть отрицательным")
            continue
        return value


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "todos.json"
    try:
        todos = load_todos(source)

        counts = completion_counts(todos)
        leaders = top_users(counts)
        leaders_done = leader_tasks(todos, leaders)

        print("Выполнено задач по пользователям:")
        for user in sorted(counts):
            print(f"  пользователь {user}: {counts[user]}")
        print("Лидеры:", ", ".join(str(user) for user in leaders) or "нет")

        user_id = read_user_id()
        threshold = read_threshold()
        selected = select_tasks(todos, user_id, threshold)
        print(f"Незавершённые задачи пользователя {user_id} "
              f"с названием не короче {threshold}: "
              f"{[todo['id'] for todo in selected]}")

        # Файлы результатов трогаем только после успешной обработки входа.
        dump_json(folder / "leaders.json", leaders_done)
        dump_json(folder / "selected.json", selected)
        print("Результаты сохранены: leaders.json, selected.json")
    except FileNotFoundError:
        print(f"Файл не найден: {source.name}")
    except UnicodeError:
        print("Неверная кодировка файла (нужен UTF-8)")
    except json.JSONDecodeError as error:
        print(f"Некорректный JSON: {error}")
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")


if __name__ == "__main__":
    main()
