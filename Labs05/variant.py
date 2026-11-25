# Номер варианта (1-15). Поменяйте на свой.
VARIANT = 1

text = input("Введите текст: ")

count = 0

for word in text.split():
    # Убираем знаки препинания по краям и приводим к нижнему регистру
    clean = word.strip(".,!?;:").lower()

    # Пустые результаты пропускаем (дальше можно безопасно брать clean[0] и clean[-1])
    if clean == "":
        continue

    match = False

    if VARIANT == 1:
        match = clean.startswith("а")
    elif VARIANT == 2:
        match = clean.endswith("я")
    elif VARIANT == 3:
        match = len(clean) >= 5
    elif VARIANT == 4:
        match = clean.startswith("к")
    elif VARIANT == 5:
        match = clean.endswith("а")
    elif VARIANT == 6:
        match = len(clean) == 4
    elif VARIANT == 7:
        match = "р" in clean
    elif VARIANT == 8:
        match = clean.count("а") == 1
    elif VARIANT == 9:
        match = "а" not in clean
    elif VARIANT == 10:
        match = clean[0] == clean[-1]
    elif VARIANT == 11:
        match = 3 <= len(clean) <= 5
    elif VARIANT == 12:
        match = "ра" in clean
    elif VARIANT == 13:
        match = clean.endswith("й")
    elif VARIANT == 14:
        match = len(clean) % 2 == 0
    elif VARIANT == 15:
        match = clean[0] in "аеёиоуыэюя"

    if match:
        print(clean)
        count += 1

if count == 0:
    print("Нет совпадений")
print(f"Количество: {count}")
