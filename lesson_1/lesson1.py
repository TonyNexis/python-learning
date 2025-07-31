# Присвоєння змінним якихось значень та вивід на екран

name = 'Anton'
surname = 'Tymchyk'
age = 34
print("Ім'я:", name, '\nПрізвище:', surname, '\nВік:', age)

print('\n')

# Калькулятор

usd_rate = 42.5
uah_amount = int(input("Введіть суму: "))

result = usd_rate * uah_amount

if result.is_integer():
    print(f"Ви отримаєте: {int(result)} гривень") 
else:
    print(f"Ви отримаєте: {result:.2f} гривень") 