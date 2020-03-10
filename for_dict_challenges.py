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
# students = [
#   {'first_name': 'Вася'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Оля'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Петя'},
# ]

# name_dict = {}
# for student in students:
#     name = student['first_name']
#     if name not in name_dict:
#         name_dict[name] = 1
#     else:
#         name_dict[name] = name_dict[name] + 1
# print(name_dict)
# max_name = list(name_dict.values())
# name_list = list(name_dict.keys())
# print(f'Самое частое имя среди учеников: {name_list[max_name.index(max(max_name))]}')

# Пример вывода:
# Самое частое имя среди учеников: Маша
        

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# school_students = [
#   [  # это – первый класс
#     {'first_name': 'Вася'},
#     {'first_name': 'Вася'},
#   ],
#   [  # это – второй класс
#     {'first_name': 'Маша'},
#     {'first_name': 'Маша'},
#     {'first_name': 'Оля'},
#   ]
# ]
# name_dict1 = {}
# name_dict2 = {}
# for student in school_students[0]:
#     name_ppl = student['first_name']
#     if name_ppl not in name_dict1:
#         name_dict1[name_ppl] = 1
#     else:
#         name_dict1[name_ppl] += 1
# max_name1 = list(name_dict1.values())
# name_list1 = list(name_dict1.keys())
# print(f'Самое частое имя среди учеников: {name_list1[max_name1.index(max(max_name1))]}')
# for student in school_students[1]:
#     name_ppl = student['first_name']
#     if name_ppl not in name_dict2:
#         name_dict2[name_ppl] = 1
#     else:
#         name_dict2[name_ppl] += 1
# max_name2 = list(name_dict2.values())
# name_list2 = list(name_dict2.keys())
# print(f'Самое частое имя среди учеников: {name_list2[max_name2.index(max(max_name2))]}')

# class_number = 1              
# for student in school_students:
#     name_dict = {}
#     for name_students in student:
#         name_ppl = name_students['first_name']
#         if name_ppl not in name_dict:
#             name_dict[name_ppl] = 1
#         else:
#             name_dict[name_ppl] += 1 
#     max_name = list(name_dict.values())
#     name_list = list(name_dict.keys())
#     print(f'Самое частое имя среди учеников {class_number} класса: {name_list[max_name.index(max(max_name))]}')
#     class_number += 1

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for classes in school:
    name_list = []
    girls_count = 0
    boys_count = 0
    for names in classes['students']:
        name_list.append(names['first_name'])
    for name in name_list:
        if is_male[name] is False:
            girls_count += 1
        else:
            boys_count += 1
        
    print(f'В классе {classes["class"]} {girls_count} девочек и {boys_count} мальчиков')
       


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a   
