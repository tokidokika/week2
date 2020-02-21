"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
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
  
  
if __name__ == "__main__":
	main()