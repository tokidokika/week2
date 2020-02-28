# with open('myfile1354.txt', 'r', encoding='utf-8') as myfile:
#     for line in myfile:
#         line = line.title()
#         line = line.replace('\n', '')   #убираем перевод строки из файла
#         print(line)



with open('referat.txt', 'r', encoding='utf-8') as newfile:
    
    content = newfile.read()
    contetn_ln = len(content)
    print(contetn_ln)              # результат 1509

    word_ln = content.split()
    word_ln = len(word_ln)
    print(word_ln)

    line = content.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as files:
        files.write(line)
           
