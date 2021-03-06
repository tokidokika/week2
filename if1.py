"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def ages(years):
      par1 = abs(int(years))
      if 0 <= par1 <= 6:
          return 'Деятельность: детский сад'
      elif 7 <= par1 < 18:
          return 'Деятельность: школа'
      elif 18 <= par1 <= 22:
          return 'Деятельность: ВУЗ'
      else:
          return 'Деятельность: работа'

    age = int(input('Введите интересующий вас возраст: '))
    quest = ages(age)
    print(quest)

if __name__ == "__main__":
    main()
