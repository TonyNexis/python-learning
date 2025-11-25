#testing features
# print('Hello world')
# print("Hell\o \w\o\\rl\d")
# print('\t')
# print("Hello\s wo\\rld")

# print(5 + 5, 10, 24, sep=', ', end='.')
# print (12 ** 5)
# print(min(2, 4, 5, 6, 0))
# print(max(2, 4, 5, 6, 0))
# print(pow(12, 5))
# print(round(12.6))
# input('Enter number: ')

# a = int(input('Enter age: '))
# admin = True

# if a > 18 and admin:
#     print('You can enter')
# elif a == 18 and admin:
#     print('bingo')
# else: 
#     print('Your age is too low')

# accessGranted = True if a >= 18 else False

# print(f'Access granted: {accessGranted}')

# if not admin:
#     print('access denied')
# else:
#     print('access granted')

# for i in range(10, 16, 2):
#     print(i)

# word = 'abccccdec'
# a = 0
# for i in word:
#     if i == 'c':
#         a += 1
# print(f'found {a} letters')

# b = 110

# while b < 10:
#     b += 1
#     print(b) 

# enter = True

# while enter:
#     user_input = input('Print something: ')
#     if user_input == 'stop':
#         enter = False

# print('System stop')

# text = input('Enter text: ')
# matchCount = 0
# matched = False

# for i in text:
#     if i == 'a':
#         matched = True
#         print('match a')
#         break
#     elif i == 'b':
#         matched = True
#         matchCount += 1

# if matchCount > 0:
#     print(f'match b: {matchCount}')

# if not matched:
#     print('not found')

# workers = ['Anton', 'Vova', 'Tony', 'Mark']

# # workers[0] = 'Jhon'
# workers.append('Olja')
# # workers.insert(2, False)
# # workers.extend(['t', 'a', 's'])
# workers.sort(key=str.lower)

# print(len(workers))

# for i in range(len(workers)):
#     # workers[i] += 'SS'
#     print(i, workers[i])

# count_employes = int(input('Enter number: '))

# i = 0

# employes = []

# if count_employes <= 0:
#     print('No employes')
# else:
#     while i < count_employes:
#         text = f'Enter name employer {i + 1}: '
#         employes.append(input(text))
#         i += 1

# employes.sort(key=str.lower)
# print(employes)

# input = 'lviv,kiev,wroclaw'
# list = input.split(',')

# for i in range(0, len(list)):
#     list[i] = list[i].capitalize()

# result = ', '.join(list)
# print(result)

# user = {'name': "Alex", 
#         "age": 33, 
#         'admin': False}
# print(user['name'])
# user2 = dict(
#     name = 'Tony',
#     age = '22',
#     admin = True
# )

# for el in user2.values():
#     print(el) 

# testData = {23, 44, 5, 1, 'ALex', 'asdasd', 'hj'}
# testData.update('vova')
# print(testData)


class User:
    __name: str
    __age: int
    __city: str

    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city

    def get_info(self):
        return f'n: {self.__name}, a: {self.__age}, c: {self.__city}'
    
class SuperUser(User):
    __premium = True

    def __init__(self, name, age, city, premium=True):
        super().__init__(name, age, city)
        self.__premium = premium

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info} | Premium: {self.__premium}'

class Admin(User):
    pass

class Moder(User):
    pass
    
user1 = User("Anton", 33, 'Lviv')
user2 = SuperUser('Nick', '22', 'London')
user2.__name = 'Kiki'
# print(user1.get_info())
print(user2.get_info())
# print(user2.premium)


class Building:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.__year = year
        self.__city = city
        # self.get_info()

    def get_info(self):
        print(f'Year: {self.__year}, City: {self.__city}')

class School(Building):
    __pupils = None

    def __init__(self, year, city, pupils=500):
        super().__init__(year, city)
        self.__pupils = pupils

    def get_info(self):
        super().get_info()
        print(f'Pupils: {self.__pupils}')

class House(Building):
    pass

class Shop(Building):
    pass


school = School(1999, 'Lviv', 760)
school.pupils = 1
school.get_info()
house = Shop(1980, 'Lviv')
house.get_info()
shop = Building(2005, 'Kiev')