word_text = ['разработка', 'сокет', 'декоратор']
unicode_txt = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
               '\u0441\u043e\u043a\u0435\u0442',
               '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for i in range(0, len(word_text)):
    print(f'{type(word_text[i])} - {word_text[i]}')
    print(f'{type(unicode_txt[i])} - {unicode_txt[i]} <- unicode')
print('-------------- кодовые точки програмно ------------')
for i in word_text:
    out_txt = ''
    for j in range(0, len(i)):
        out_txt += r'\u{:04X}'.format(ord(i[j]))
    print(f'{i} -> {out_txt}')
