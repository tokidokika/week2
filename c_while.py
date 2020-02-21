# x = 1
# while x < 5:
#     print(x)
#     x += 1


while True:
    user_say = input('Скажи что-нибудь: ')
    if user_say == 'Пока':
        print('Ну пока')
        break
    else:
        print(f'Сам ты {user_say}')
