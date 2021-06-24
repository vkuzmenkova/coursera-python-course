from sys import stdin
import copy as cp


class Matrix:
    def __init__(self, list_of_lists=None):
        if list_of_lists is None:
            list_of_lists = []
        else:
            self.list_of_lists = cp.deepcopy(list_of_lists)

    def __str__(self):
        matrix_str = ''
        for inner_list in self.list_of_lists:
            for number in inner_list:
                matrix_str += f"{number}\t"
            matrix_str = matrix_str[0:-1]
            matrix_str += '\n'

        matrix_str = matrix_str[0:-1]

        return matrix_str

    def size(self):
        return len(self.list_of_lists), len(self.list_of_lists[0])


exec(stdin.read())
