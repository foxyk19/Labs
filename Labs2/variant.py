total = int(input("Общий объём: "))
capacity = int(input("Вместимость одной единицы: "))

full_units = total // capacity
remainder = total % capacity
needed_units = (total + capacity - 1) // capacity

print("Полных единиц:", full_units)
print("Остаток:", remainder)
print("Минимальное число единиц:", needed_units)
