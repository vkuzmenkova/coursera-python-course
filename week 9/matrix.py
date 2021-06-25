from sys import stdin
import copy as cp


class Matrix:
    def __init__(self, in_list=None):
        if in_list is None:
            self.in_list = []
        else:
            self.in_list = cp.deepcopy(in_list)

    def __str__(self):
        matrix_str = ''
        for inner_list in self.in_list:
            for number in inner_list:
                matrix_str += f"{number}\t"
            matrix_str = matrix_str[0:-1]
            matrix_str += '\n'

        matrix_str = matrix_str[0:-1]

        return matrix_str

    def __add__(self, other):

        if self.size() == other.size():

            res_matrix = []
            for i in range(self.size()[0]):
                line = []
                for j in range(self.size()[1]):
                    line.append(self.in_list[i][j] + other.in_list[i][j])
                res_matrix.append(line)

            return Matrix(res_matrix)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):

        res_matrix = []

        for i in range(self.size()[0]):
            res_line = []
            for j in range(self.size()[1]):
                res_line.append(self.in_list[i][j] * other)
            res_matrix.append(res_line)

        return Matrix(res_matrix)

    __rmul__ = __mul__

    def size(self):
        return len(self.in_list), len(self.in_list[0])

    def transpose(self):

        res_matrix = []

        for j in range(self.size()[1]):
            res_line = []
            for i in range(self.size()[0]):
                res_line.append(self.in_list[i][j])
            res_matrix.append(res_line)

        self.in_list = res_matrix

        return self

    @staticmethod
    def transposed(matrix):

        res_matrix = []

        for j in range(matrix.size()[1]):
            res_line = []
            for i in range(matrix.size()[0]):
                res_line.append(matrix.in_list[i][j])
            res_matrix.append(res_line)

        return Matrix(res_matrix)


class MatrixError(Exception):

    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


exec(stdin.read())
