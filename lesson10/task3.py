word_txt = ['attribute', 'класс', 'функция', 'type']
index = 0
while index < len(word_txt):
    try:
        print(bytes(word_txt[index], 'ascii'))
    except Exception as e:
        print(f'Слово КИРИЛИЦЕЙ: {e.args[1]} - невозможно записать в байтовом типе в кодировке ASCII')
    finally:
        index += 1
