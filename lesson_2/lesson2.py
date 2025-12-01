# client_type = 'basic'
# order_amount = 1001

# discount = (
#     0.2 if client_type == 'premium' and order_amount > 750 else
#     0.1 if client_type == 'basic' and order_amount > 1000 else
#     0
# )

# final_price = order_amount * (1 - discount)

# print(f'Тип клієнта: {client_type} \n Сумма замовлення: {order_amount} грн. \n Знижка: {round(discount * 100)}% \n Фінальна ціна: {final_price} грн.')

password = 'hello'
counter = 3

while counter >= 1:
    inputPassword = input('Введіть пароль: ')
    if inputPassword == password:
        print('Удача, пароль правильний')
        break
    else:
        counter -= 1
        if counter >= 1:
            print(f'Помилка, у вас лишилось {counter} спроб')
        
if counter < 1:
    print('Ви перевищили ліміт спроб!')
    