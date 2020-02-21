"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    q_and_a = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Пока": "Бывай"}
    def ask_user_dict():
        while True:
          try:
            user_say = input('Введите вопрос: ')
            if user_say in q_and_a.keys():
                print(q_and_a[user_say])
            else:
                print('Не понимаю')
          except KeyboardInterrupt:
            print('Пока')
            break
    ask_user_dict()
    
if __name__ == "__main__":
    ask_user()
