"""Офлайн-режим HTTP-упражнения: чтение учебного профиля profile_sample.json."""
import json
from pathlib import Path


def main():
    path = Path(__file__).resolve().parent / "profile_sample.json"
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Файл profile_sample.json не найден")
    except (ValueError, OSError) as error:
        print(f"Не удалось прочитать файл: {error}")
    else:
        print("Использованы учебные локальные данные (сеть не применялась)")
        print(f"Логин: {data['login']}")
        # null (None) не заменяем выдуманными данными
        print(f"Имя: {data['name']}")


if __name__ == "__main__":
    main()
