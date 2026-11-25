first_room = input("Название первой аудитории: ")
second_room = input("Название второй аудитории: ")

print("Исходные значения:")
print("Первая аудитория:", first_room)
print("Вторая аудитория:", second_room)

temporary_room = first_room
first_room = second_room
second_room = temporary_room

print("Изменённые значения:")
print("Первая аудитория:", first_room)
print("Вторая аудитория:", second_room)
