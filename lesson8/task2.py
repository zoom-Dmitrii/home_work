'''
Задача 2.
Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.
'''
import json
from inputkey import input_natural, input_float, input_txt, get_date

'''
Что должно добавляться к имеющейся записи:
"item": "принтер",
"quantity": "10",
"price": "6700",
"buyer": "Ivanov I.I.",
"date": "24.09.2017"
'''

file_orders = 'orders.json'


def rider_order_is_json():
    with open(file_orders, 'r') as work_file:
        return json.loads(work_file.read())


def write_order_to_json(**kwargs):
    work_orders = rider_order_is_json()
    work_orders["orders"].append(kwargs)
    with open(file_orders, 'w') as work_file:
        json.dump(work_orders, work_file, sort_keys=False, indent=4)
    return


write_order_to_json(item=input_txt('Введите название товара: '),
                    quantity=input_natural('Введите количество товара: '),
                    price=input_float('Введите цену за единицу товара: '),
                    buyer=input_txt('Введите данные покупателя: '),
                    date=get_date())
