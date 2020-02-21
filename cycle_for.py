# for number in range(3):
#     print(f'Привет мир {number}!')


# for letter in 'python':
#     print(letter.upper())


# example_string = 'Я учу язык python'
# for word in example_string.split() :
#     print(f'Длина слова "{word}": {len(word)}')


# students_scores = [1, 21, 19, 6, 5]
# for score in students_scores:
#     print(score)


# students_scores = [1, 21, 19, 6, 5]
# # print(f'Средняя оценка: {sum(students_scores)/len(students_scores)}')
# scores_sum = 0
# for score in students_scores:
#     scores_sum += score
#     print(scores_sum)
# print(f'Средняя оценка: {scores_sum/len(students_scores)}')


# from operator_if import discounted

# stock = [
# 		{'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25},
# 		{'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10},
# 		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
# ]

# # for phone in stock:
# #     print(phone)
# #     phone['final_price'] = discounted(phone['price'], phone['discount'], name=phone['name'])
# #     print(phone)
# #     print('---')

# for phone in stock:
#     phone['final_price'] = discounted(phone['price'], phone['discount'], name=phone['name'])
#     print(stock)


# numb = [20, 5, 35, 12, 74, 1, 95, 45, 69, 37]
# for cycle in numb:
#     cycle +=1
#     print(cycle)


school_classes = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
      {'school_class': '8б', 'scores': [5, 2, 4, 5, 4]},
      {'school_class': '10а', 'scores': [4, 4, 3, 5, 3]}
    ]
avg_scores_sch = 0
for each_scores in school_classes:
    avg_scores = sum(each_scores['scores'])/len(each_scores['scores'])
    class_name = each_scores['school_class']
    print(f'Средний балл по классу {class_name} составляет {avg_scores}')
    avg_scores_sch += avg_scores
    print(avg_scores_sch)


   