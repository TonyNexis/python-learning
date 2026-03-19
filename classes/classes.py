from dataclasses import dataclass
# # from typing import ClassVar


# # class Test: 
# #     def __init__(
# #             self,
# #             side_text,
# #             main_color,
# #             additional_colors,
# #             autopilot
# #     ):
# #         self.side_text = side_text
# #         self.main_color = main_color
# #         self.additional_colors = additional_colors
# #         self.autopilot = autopilot

# #     def view_info(self):
# #         print(f'some info ==> {self.side_text}')

# # @dataclass(frozen=True)
# # class Plane:
# #     wings_count: ClassVar[int] = 2

# #     side_text: str
# #     main_color: str
# #     additional_colors: str
# #     autopilot: bool

# #     @classmethod
# #     def changewings_num(cls, new_wings_count: int):
# #         cls.wings_count = new_wings_count

# # raptor = Test(
# #     side_text='Raptor 323',
# #     main_color='red',
# #     additional_colors=['black', 'white'],
# #     autopilot='false'
# # )

# # boing = Plane('boing 123', 'white', 'blue', True)
# # kukuruza = Plane('Kukuruza 1', 'black', 'white', False)

# # # print(f'Raptor colors ->> {', '.join(raptor.additional_colors)}')
# # # print(f'Boing ->> {boing}')
# # boing.changewings_num(3)
# # print(boing.wings_count)
# # print(kukuruza.wings_count)


# user_name = 'Anton'
# user_age = 35
# languages = ['Python', 'Javascript', 'Typescript']

# # print(f'Привіт, мене звати {user_name}, мені {user_age} років і я вчу {languages[0]}')

# experience_years = 0

# if experience_years >= 2:
#     print('Ти вже Middle розробник!')
# elif experience_years > 0:
#     print('Ти впевнений Junior!')
# else:
#     print('Ти на початку шляху, успіхів у навчанні!')

# if "Python" in languages:
#     print('О, ти обрав правильну мову!')

# tech_stack = ["Python", "FastAPI", "SQL", "Docker", "Linux"]

# for i in tech_stack:
#     if i == 'Python':
#         print(f'{i} - це основа!')
#     elif i == 'Docker':
#         print(f'{i} - це складно, але корисно!')
#     else:
#         print(f'Вивчаю {i}...')

# secret_password = "python123"
# user_input = ''
# attempts = 0

# # while user_input != secret_password:
# #     attempts += 1
# #     print(f'Спроба №{attempts}...')
# #     user_input = input('Введіть пароль: ')

# # print(f'Доступ дозволено! Кількість ваших спроб: {attempts}')

# def get_long_names(names: list[str]) -> list[str]:
#     """
#     Фільтрує список імен, залишаючи лише ті, що мають більше 5 символів.

#     Args:
#         names (list[str]): Список імен (рядків), які потрібно перевірити.

#     Returns:
#         list[str]: Новий список, що містить лише імена довжиною понад 5 символів.
#     """

#     result = []

#     for name in names:
#         if len(name) > 5:
#             result.append(name)

#     return result

# some_names = ["Vova", "Anton", "Jakonda", "Valentina", "Volodimir"]

# print(get_long_names(some_names))

# def new_test_func(names: list[str]) -> list[str]:
#     return [name for name in names if len(name) > 5]

# print(new_test_func(some_names))

# def convert_prices(prices: list[float]) -> list[float]:
#     """Конвертує ціни > 1000 грн у долари."""
#     return [price/40 for price in prices if price > 1000]

# price_list = [400.0, 2000.0, 80.0, 4000.0]

# print(convert_prices(price_list))

# items = [
#     {"name": "Phone", "price": 15000},
#     {"name": "Case", "price": 500},
#     {"name": "Laptop", "price": 45000},
#     {"name": "Cable", "price": 300}
# ]

# dirty_items = [
#     {"name": "Phone", "price": 15000},
#     {"price": 50000},  # Немає імені
#     {"name": "Mystery Box"},  # Немає ціни
#     {"name": "Case", "price": 200}
# ]


# class BankAccount:
#     def __init__(self, owner: str, balance: float = 0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount: float):
#         self.balance += amount
#         print(f'Рахунок поповнено на {amount}. Новий баланс: {self.balance}')
    
#     def withdraw(self, amount: int):
#         if amount > self.balance:
#             print('Недостатньо коштів на рахунку!')
#             return
#         self.balance -= amount
#         print(f'З рахунка знято {amount}, Новий баланс: {self.balance}')

# my_acc = BankAccount("Taras", 1000)
# my_acc.deposit(500)
# my_acc.withdraw(200) # Має написати про нестачу коштів

# class SavingsAccount(BankAccount):
#     def __init__(self, owner: str, balance: float, interest_rate: float):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     def add_interest(self):
#         interest_amount = self.balance * (self.interest_rate / 100)
#         self.deposit(interest_amount)

@dataclass
class BankAccount:
    owner: str
    balance: float = 0.0

    def deposit(self, amount: float):
        self.balance += amount
        print(f'Рахунок поповнено на {amount}. Новий баланс: {self.balance}')


    def withdraw(self, amount: float):
        if amount > self.balance:
            print('Недостатньо коштів на рахунку!')
            return
        self.balance -= amount
        print(f'З рахунка знято {amount}, Новий баланс: {self.balance}')



@dataclass
class SavingsAccount(BankAccount):
    interest_rate: float = 0.0

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.deposit(interest_amount)

tony = SavingsAccount('Tony', 2000, 10)
tony.add_interest()

