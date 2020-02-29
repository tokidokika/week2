# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

# students = [
#   {'first_name': 'Вася'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Рома'}
# ]

# name_dict = {}

# for student in students:
#     name = student['first_name']
#     if name not in name_dict:
#         name_dict[name] = 1
#     elif name in name_dict:
#         name_dict[name] = name_dict[name] + 1

# for key, value in name_dict.items():
#     print(f'{key}: {value}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

students_list = []
name_dict = {}
for student in students:
    name = student['first_name']
    if name not in name_dict:
        name_dict[name] = 1
    else:
        name_dict[name] = name_dict[name] + 1

for key, value in name_dict.items():
    print(f'{key}: {value}')
    if value > 1:
        print(f'частое имя среди учеников: {key}')


# Пример вывода:
# Самое частое имя среди учеников: Маша
        
    
