n = int(input("Введите n: "))
count = 0
sum_all = 0

for i in range(n):
    value = int(input("Введите число: "))
    if value % 2 == 0:
        count += 1
        sum_all += value

print("Количество:", count)
print("Сумма:", sum_all)
