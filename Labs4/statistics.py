n = int(input("Введите количество чисел: "))

sum_all = 0
positive_count = 0
maximum = None

for i in range(n):
    value = int(input("Введите число: "))
    sum_all += value
    if value > 0:
        positive_count += 1
    if maximum is None or value > maximum:
        maximum = value

print("Сумма:", sum_all)
print("Положительных:", positive_count)
print("Максимум:", maximum)
