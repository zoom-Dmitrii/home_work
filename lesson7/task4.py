# Задание 4
from inputkey import input_matrix


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for ind_1 in self.matrix:
            res += f'{ind_1}\n'
        return res

    def __add__(self, other):
        result_matrix = []
        for in_1 in range(len(self.matrix)):
            new_el = []
            for in_2 in range(len(self.matrix[in_1])):
                new_el.append(self.matrix[in_1][in_2] + other.matrix[in_1][in_2])
            result_matrix.append(new_el)
        return Matrix(result_matrix)


# Созданные матрицы хранятся в списке matrix_list
print('Создание матриц через класс. Сложение матриц')
matrix_list = []
new_matrix = input_matrix('Введите размер матриц, цифры через пробел: ')
matrix_list.append(Matrix(new_matrix))
new_matrix = input_matrix(f'Вторая матрица', (len(new_matrix)), len(new_matrix[0]))
matrix_list.append(Matrix(new_matrix))
print('Первая матрица')
print(matrix_list[0])
print('Вторая матрица')
print(matrix_list[1])
matrix_list.append(matrix_list[0] + matrix_list[1])
print('Сумма двух матриц')
print(matrix_list[2])
