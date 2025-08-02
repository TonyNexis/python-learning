a = input('Введіть значення: ')

print(a[::3])
print(a[0].upper())

# -----------------

surname = input('Введіть прізвище: ')
first_name = input("Введіть ім'я: ")
patronymic = input('Введіть по батькові: ')

print(f"{surname.title()} {first_name.title()} {patronymic.title()}")