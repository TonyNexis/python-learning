# # Присвоєння змінним якихось значень та вивід на екран

# name = 'Anton'
# surname = 'Tymchyk'
# age = 34
# print("Ім'я:", name, '\nПрізвище:', surname, '\nВік:', age)

# print('\n')

# # Калькулятор

# usd_rate = 42.5
# uah_amount = int(input("Введіть суму: "))

# result = usd_rate * uah_amount

# if result.is_integer():
#     print(f"Ви отримаєте: {int(result)} гривень") 
# else:
#     # print(f"Ви отримаєте: {result:.2f} гривень") 
#     print(f"Ви отримаєте: {round(result, 2)} гривень") 



def month(month_num):
    months = ['January', 'February', 'March', 'April', 'May']
    try:
        month_index = abs(month_num) - 1
        return months[month_index]
    except TypeError:
        return 'Please use only integers'
    except IndexError:
        return 'Please use integers between 1 and 5'
    

print(month(123))

assert month(2) == 'February'
