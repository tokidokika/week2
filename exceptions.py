# def cut_cake(people):
#     try:
#         parts = 1 / people
#         print(f'Каждый человек получит {parts} пирога')
#     # except ZeroDivisionError:
#     #     print('Не надо делить на ноль')
#     # except TypeError:
#     #     print('Только числа')
#     except (ZeroDivisionError, TypeError):
#         print('Не могу поделить')

# cut_cake('5')

# import random

# def cut_cake(people):
#     try:
#         parts = 1 / people
#         print(f'Каждый человек получит {parts} пирога')
#     except (ZeroDivisionError, TypeError):
#         print('Не могу поделить')

# while True:
#     p = random.randint(1, 10)
#     cut_cake(p)


def discounted(price, discount, max_discount=50):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Максимальная скидка не может быть больше 99%')
        if discount >= max_discount:
            price_with_discount = price
        else:
            price_with_discount = price - (price * discount / 100)
        return price_with_discount
    except ValueError:
        print('Не все параметры – числа')

# product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 70}
# product['with_discount'] = discounted(product['price'], product['discount'], max_discount=80)
# print(product)
# discounted(100, 50, max_discount=100)
print(discounted(100, 40))
print(discounted('3', 4))
print(discounted('azaz', 'neazaz'))