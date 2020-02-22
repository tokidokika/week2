import ephem

# mars = ephem.Mars('2000/01/01')
# const = ephem.constellation(mars)

# print(const)

'''Написать функцию, которая при вводе планеты пользователем выдаёт ее положение в созвездии на today'''

def planets(planet):
    date = '2000/01/01'
    user_say = planet
    dct = {
        'Pluto': ephem.Pluto
    }
    planet_func = dct[user_say]
    planet_obj = planet_func(date)
    planet_cons = ephem.constellation(planet_obj)
    print(planet_cons[1])
    # if user_say == 'Pluto':
    #     plt = ephem.Pluto(date)
    #     print(user_say, date, ephem.constellation(plt))
    # elif user_say == 'Mercury':
    #     mrc = ephem.Merc(date)
    #     # print(user_say 'на дату' date, ephem.constellation(plt)

planets('Pluto')