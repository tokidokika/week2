from collections import Counter

phones = ['Iphone', 'Samsung', 'LG', 'Iphone', 'Iphone', 'LG']
count = Counter(phones)
print(count)
print(count['LG'])
print(count['Hello'])



text = 'Ехал Грека через реку видит Грека в реке рак'
# count = Counter(text)
# print(count)
count = Counter(text.lower().replace(' ', ''))   # Можно сразу делать в переменной text = 'Ехал Грека через реку видит Грека в реке ракlower().replace(' ', '')'
print(count)