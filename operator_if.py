# balance = -10
# print(bool(balance < 0))
# if balance < 0:
#     print('Пожалуйста, пополните баланс!')


# balance = 100
# price = 200
# print(bool(balance < 0 or price > balance))
# if balance < 0 or price > balance:
#     print('Пополните баланс')


# balance = 1000
# price = 2000
# if balance > price:
#     print('Спасибо за покупку')
# else:
#     print('Пополните баланс')



# def weather(temperature):
#     if temperature <= 0:
#         return 'На улице холодно'
#     elif 1 <= temperature <= 15:
#         return 'На улице прохладно'
#     elif 16 <= temperature <= 25:
#         return 'На улице тепло'
#     else:
#         return 'На улице жарко'

# print(weather(15))
# print(weather(10))
# print(weather(-10))



# phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 15}
# phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}
# phone3 = {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}

def discounted(price, discount, max_discount=20, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or 'iphone' in name.lower() or not name:
        return price
    else:
        return price - (price * discount / 100)

# apple_desc = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
# print(apple_desc)

# android_desc = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
# print(android_desc)

# noname_desc = discounted(phone3['price'], phone3['discount'], name=phone3['name'])
# print(noname_desc)



# def ages(years):
#     par1 = abs(int(years))
#     if 0 <= par1 <= 6:
#         return 'Деятельность: детский сад'
#     elif 7 <= par1 < 18:
#         return 'Деятельность: школа'
#     elif 18 <= par1 <= 22:
#         return 'Деятельность: ВУЗ'
#     else:
#         return 'Деятельность: работа'

# age = int(input('Введите интересующий вас возраст: '))
# quest = ages(age)
# print(quest)


def compar(par1, par2):
    if type(par1) is str and type(par2) is str:                        
        if par1 == par2:
            return '1'
        elif len(par1) > len(par2):
            return '2'
        elif par2 == 'learn':
            return '3'
        # else:
        #     return '0'
    else:
        return '0'

inpt = input('Введите данные 1 параметра: ')
inpt1 = input('Введите данные 2 параметра: ')
parameters = compar(inpt, inpt1)
print(parameters)
# print(compar(1, '100'))