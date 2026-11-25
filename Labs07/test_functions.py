from functions import average, normalize_text, select_numbers, sum_digits

# Базовые проверки
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# Исходный список после average() не изменился
data = [3, 1, 2]
saved = data.copy()
average(data)
assert data == saved

# Вариант 1: числа больше порога
# (если у вас другой вариант, замените ожидаемые значения ниже
#  по таблице из задания и поменяйте VARIANT в functions.py)
assert select_numbers([-5, 0, 2, 5], 2) == [5]
assert select_numbers([1, 2, 3, 4], 2) == [3, 4]
assert select_numbers([], 2) == []
assert select_numbers([-5, 0, 2], 2) == []

# Граница условия и значения рядом с ней
assert select_numbers([1, 2, 3], 2) == [3]
assert select_numbers([-1, 0, 1], 0) == [1]

# Повторы сохраняются, порядок не меняется
assert select_numbers([3, 5, 3, 1, 3], 2) == [3, 5, 3, 3]

# Исходный список после вызова не изменился
numbers = [-5, 0, 2, 5]
saved_numbers = numbers.copy()
result = select_numbers(numbers, 2)
assert numbers == saved_numbers
assert result is not numbers

print("Базовые проверки пройдены")
