order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

position_1_name = input("Название первой позиции: ")
position_1_quantity = int(input("Количество первой позиции: "))
position_1_price = float(input("Цена одной первой позиции в рублях: "))

position_2_name = input("Название второй позиции: ")
position_2_quantity = int(input("Количество второй позиции: "))
position_2_price = float(input("Цена одной второй позиции в рублях: "))

delivery_cost = float(input("Стоимость доставки в рублях: "))
paid_amount = float(input("Внесённая сумма в рублях: "))

position_1_cost = position_1_quantity * position_1_price
position_2_cost = position_2_quantity * position_2_price
goods_cost = position_1_cost + position_2_cost
total_cost = goods_cost + delivery_cost
total_quantity = position_1_quantity + position_2_quantity
change = paid_amount - total_cost

discount_percent = float(input("Скидка в процентах от стоимости товаров: "))
discount_amount = goods_cost * discount_percent / 100
discounted_goods_cost = goods_cost - discount_amount
new_total_cost = discounted_goods_cost + delivery_cost
new_change = paid_amount - new_total_cost

print("\nЗаголовок заказа:", order_name)
print("Имя заказчика:", customer_name)
print(f"{position_1_name} | {position_1_quantity} | {position_1_price:.2f} | {position_1_cost:.2f}")
print(f"{position_2_name} | {position_2_quantity} | {position_2_price:.2f} | {position_2_cost:.2f}")
print("Стоимость товаров без доставки:", f"{goods_cost:.2f}")
print("Общая стоимость с доставкой:", f"{total_cost:.2f}")
print("Общее количество единиц:", total_quantity)
print("Сдача:", f"{change:.2f}")
print("Размер скидки:", f"{discount_amount:.2f}")
print("Новая итоговая стоимость:", f"{new_total_cost:.2f}")
print("Новая сдача:", f"{new_change:.2f}")
