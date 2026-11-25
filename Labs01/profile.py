surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст в полных годах (1–120): "))
subject = input("Любимый предмет: ")
hours = float(input("Количество часов подготовки в неделю: "))

age_in_four_years = age + 4
hours_for_four_weeks = hours * 4
average_daily_hours = hours / 7

print("\nКАРТОЧКА СТУДЕНТА")
print(f"Фамилия: {surname}")
print(f"Имя: {name}")
print(f"Полное имя: {name} {surname}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст: {age}")
print(f"Возраст через четыре года: {age_in_four_years}")
print(f"Любимый предмет: {subject}")
print(f"Часы подготовки в неделю: {hours:.2f}")
print(f"Время подготовки за четыре недели: {hours_for_four_weeks:.2f} часов")
print(f"Среднее время подготовки в день за семидневную неделю: {average_daily_hours:.2f} часов")
