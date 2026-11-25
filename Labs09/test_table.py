from table import column_sums, diagonal_pattern, row_sums, transform

# Обычная матрица 2x3
m = [[1, 2, 3], [4, 5, 6]]
assert row_sums(m) == [6, 15]
assert column_sums(m) == [5, 7, 9]

# Матрица 1x1
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

# Один столбец
col = [[1], [-1], [0]]
assert row_sums(col) == [1, -1, 0]
assert column_sums(col) == [0]

# Пустая матрица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# Узор 3x3
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

# Вариант 14: от -2 до 3 включительно возвести в квадрат
control = [[-2, 0, 3], [4, -5, 6]]
assert transform(control) == [[4, 0, 9], [4, -5, 6]]
# границы диапазона
assert transform([[-3, -2, 3, 4]]) == [[-3, 4, 9, 4]]
assert transform([[1, 2, -1]]) == [[1, 4, 1]]

# Независимость результата и неизменность исходной матрицы
original = [[-2, 0, 3], [4, -5, 6]]
snapshot = [row.copy() for row in original]
result = transform(original)
result[0][0] = 999
assert original == snapshot
assert row_sums(original) == [1, 5] and original == snapshot
assert column_sums(original) == [2, -5, 9] and original == snapshot

print("Все проверки лабораторной 9 пройдены")
