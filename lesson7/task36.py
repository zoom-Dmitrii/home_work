from inputkey import input_natural


def print_operation_table(operation, num_rows=6, num_columns=6):
    matrix = [[operation(ind_1, ind_2) for ind_2 in range(1, num_columns + 1)]
              for ind_1 in range(1, num_rows + 1)]
    for ind in matrix:
        print(''.join(f'{x:>5}' for x in ind))  # выводим значения одной строки с выравнимванием в парво


rows = input_natural('Введите количество строк матрицы: ')
columns = input_natural('Введите количество столбцов матрицы: ')
print_operation_table(lambda x, y: x * y, rows, columns)
