import csv
import os.path
import re
from glob import glob
import chardet


def get_data():
    column_name = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    file_list = [x for x in glob(os.path.join('', '*.txt')) if 'info' in x]
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
    os_name_reg = re.compile(r'[^Название ОС: ]\w*\S*[^\n]') #Название ОС:\s*\S*\s\S*
    os_code_reg = re.compile(r'Код продукта:\s*\S*')
    os_type_reg = re.compile(r'Тип системы:\s*\S*')
    for name_file in file_list:
        try:
            test_file = open(name_file, 'rb')
            rawdata = test_file.readline()
            result = chardet.detect(rawdata)
            charenc = result['encoding']
            test_file.close()
            with open(name_file, "r", encoding=charenc) as new_file:  # encoding='utf-8'
                for line in new_file:
                    if column_name[0] in line:
                        os_prod_list.append(os_prod_reg.findall(line)[0].split()[2])
                    elif column_name[1] in line:
                        str, txt = '', ''
                        for txt in list(os_name_reg.findall(line)):
                            str += txt
                        os_name_list.append(str)
                    elif column_name[2] in line:
                        os_code_list.append(os_code_reg.findall(line)[0].split()[2])
                    elif column_name[3] in line:
                        os_type_list.append(os_type_reg.findall(line)[0].split()[2])
                    else:
                        pass
        except IOError:
            print("Произошла ошибка ввода-вывода!")
    return column_name, os_prod_list, os_name_list, os_code_list, os_type_list


def write_data(file_scv):
    data_input = get_data()
    print(data_input)

    with open(file_scv, "w", newline='') as new_file:
        data_write = csv.writer(new_file)
        data_write.writerow(data_input[0])
        for i in range(len(data_input[1])):
            string_data = [i+1]
            for x in range(1, len(data_input)):
                string_data.append(data_input[x][i])
            data_write.writerow(string_data)


write_data('main_data.csv')
