'''
Задание на закрепление знаний по модулю yaml.
Написать скрипт, автоматизирующий сохранение данных
в файле YAML-формата.
'''
import yaml

file_orders = 'file.yaml'
file_test = 'file_test.yaml'


# считываем данные
def rider_order_is_jaml(file_):
    with open(file_) as work_file:
        return yaml.load(work_file, Loader=yaml.FullLoader)

# Пишем данные
def write_order_to_jaml(*args):
    with open(file_test, 'w') as work_file:
        yaml.dump(args, work_file, default_flow_style=False, allow_unicode=True)


print(rider_order_is_jaml(file_orders))  # Чтение старых данных
#  новые данные
data_in = {'Этап_€': ['первый', 'второй', 'третий', 'четвертый', 'пятый'],
           'длительность_€': 120,
           'координаты_€': {'направление': ['юг', 'север', 'восток', 'запад'], 'высота': 500}}

write_order_to_jaml(data_in)            # Запись новых данных в новый файл
print(rider_order_is_jaml(file_test))   # Проверка чтением
