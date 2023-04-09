from inputkey import input_txt


def count_vowels(str_input, vowels={'а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я'}):
    temp_count = 0
    pars_str = str_input.split(' ')
    for el in pars_str:
        count_vowel = 0
        for i in range(len(el)):
            if el[i] in vowels:
                count_vowel += 1
        if temp_count == 0:
            temp_count = count_vowel
        else:
            if temp_count != count_vowel:
                return 'Пам парам'
    return 'Парам пам-пам'


print('Фраза может состоять из одного слова, если во фразе несколько слов,'
      'то они разделяются дефисами. Фразы отделяются друг от друга пробелами')
print(count_vowels(input_txt('Введите строчку из стихотворения: ')))
