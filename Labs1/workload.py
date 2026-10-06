subject_1 = input("Название первого предмета: ")
subject_2 = input("Название второго предмета: ")

lessons_1 = int(input("Количество занятий по первому предмету за неделю: "))
lessons_2 = int(input("Количество занятий по второму предмету за неделю: "))
duration_1 = int(input("Продолжительность первого занятия в минутах: "))
duration_2 = int(input("Продолжительность второго занятия в минутах: "))

minutes_1 = lessons_1 * duration_1
minutes_2 = lessons_2 * duration_2
total_minutes = minutes_1 + minutes_2
total_hours = total_minutes / 60

available_hours = float(input("Доступное время на неделю в часах: "))
remaining_hours = available_hours - total_hours
four_week_load = total_minutes * 4 / 60

print(f"\n{subject_1}: {minutes_1} минут")
print(f"{subject_2}: {minutes_2} минут")
print(f"Общая нагрузка: {total_minutes} минут")
print(f"Общая нагрузка в часах: {total_hours:.2f}")
print(f"Остаток свободного времени: {remaining_hours:.2f} часов")
print(f"Нагрузка за четыре одинаковые недели: {four_week_load:.2f} часов")
