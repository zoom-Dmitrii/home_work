def data_user(mail=None, city=None, born=None, family=None, name=None, phon=None):
    return (f'{family} {name}, {born} года рождения, проживает в городе {city}, '
            f'email: {mail}, телефон: {phon}')


def input_txt(out_txt, txt_in=''):
    while txt_in == '':
        txt_in = input(out_txt, )
    return txt_in


def input_int(out_txt, digit=None):
    while digit is None or digit < 1900:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


print('Ввод данных пользователя: имя, фамилия, год рождения, город проживания, email, телефон')
print('')
first_name = input_txt('Имя: ')
last_name = input_txt('Фамилию: ')
year_birth = input_int('Год рождения: ')
city_birth = input_txt('Город рождения: ')
email = input('e-mail: ')
phone = input('Телефон: ')

print((data_user(phon=phone, mail=email, name=first_name, family=last_name, born=year_birth, city=city_birth)))
