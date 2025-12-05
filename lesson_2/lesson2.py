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

# while counter >= 1:
#     inputPassword = input('Введіть пароль: ')
#     if inputPassword == password:
#         print('Удача, пароль правильний')
#         break
#     else:
#         counter -= 1
#         if counter >= 1:
#             print(f'Помилка, у вас лишилось {counter} спроб')
        
# if counter < 1:
#     print('Ви перевищили ліміт спроб!')
    

# for i in range(101):
#     if i % 2:
#         continue
#     print(i)


# for i in reversed(range(100)):
#     if i % 5 == 0:
#         print(i)

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# max = test[0]

# for i in range(1, len(test)):
#     if test[i] > max:
#         max = test[i]

# print(max)

print(max(test))


books = {}

def add_books(dictionary):
    print('\n--- Додавання книги ---')
    book_title = input('Введіть назву книги: ').strip()

    if not book_title:
        print("Назва книги не може бути порожньою, спробуйте ще раз.")
        return

    while True:
        status_input = input(f'Чи прочитана книга {book_title}? (так/ні)').strip().lower()

        if status_input in ['так', 'y', 'yes', 'true', 't', 'т']:
            is_read = True
            break
        elif status_input in ['ні', 'n', 'no', 'false', 'f', 'н']:
            is_read = False
            break
        else:
            print('Невірне введеня. Будь ласка введіть "так" або "ні".')

        
    dictionary[book_title] = is_read

    print(f'\n Книгу "{book_title}" зі статусом "Прочитана: {is_read}" додано.')

add_books(books)
add_books(books)

print('\n --- Поточний список книг ---')
print(books)