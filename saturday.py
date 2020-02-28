# ''' Вывести последнюю букву в слове '''
# word = 'Архангельск'
# print(word[-1])


# Вывести количество букв "а" в слове
# word = 'Архангельск'
# print(word.lower().count('а'))


# Вывести количество гласных букв в слове
# word = 'Архангельск'.lower()
# vowels = ['а', 'е']
# letter_len = 0
# for letter in word:
#     if letter in vowels:
#         letter_len += 1
# print(letter_len)
 


# Вывести количество слов в предложении
# sentence = 'Мы приехали в гости'
# sentence_quantity = sentence.split() 
# print(len(sentence_quantity))


# Вывести первую букву каждого слова на отдельной строке
# sentence = 'Мы приехали в гости'
# split_senten = sentence.title().split(' ')
# print(split_senten)
# for word in split_senten:
#     letter_word = word[0]
#     print(letter_word)


 # Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
split_senten = sentence.split(' ')
sum_word = 0
for word in split_senten:
    len_word = len(word)
    sum_word = len_word + sum_word
avg_len = sum_word / len(split_senten)
print(avg_len)