import random


class Matrix:
    def __init__(self, size=None):
        self.size = size if size else 10
        self.x = {}
        self.y = {}
        self.z = {}
        self.sorted_x = []
        self.result = ''
        self.result_sum = 0
        self.matrix = [[[random.randrange(0, 9) for z in range(self.size)] for y in range(self.size)] for x in range(self.size)]

    def _main(self):
        self._sum_of_x()
        self._sum_of_y()
        self._sum_of_z()

    def print_matrix(self):
        return '\n'.join([('%s' % line) for line in [lines for lines in self.matrix]])

    def _sum_of_x(self):
        for i in range(self.size):
            for j in range(self.size):
                self.x['0-%s-%s' % (j+1, i+1)] = sum(self.matrix[i][j])
        self.sorted_x = self._get_sorted_list(self.x)

    def _sum_of_y(self):
        for i in range(self.size):
            for j in range(self.size):
                sum_y = 0
                for n in range(self.size):
                    sum_y += self.matrix[i][n][j]
                self.y['%s-0-%s' % (j+1, i+1)] = sum_y

    def _sum_of_z(self):
        for i in range(self.size):
            for j in range(self.size):
                sum_z = 0
                for n in range(self.size):
                    sum_z += self.matrix[n][i][j]
                self.z['%s-%s-0' % (j+1, i+1)] = sum_z

    def _get_sorted_list(self, query):
        list_of_indexes = list(query.items())
        list_of_indexes.sort(key=lambda item: item[1])
        return list(reversed(list_of_indexes))

    def calc_max_sum(self):
        self._main()
        max_elems = {}
        for line_sum_x in self.sorted_x:
            x_row = line_sum_x[0]
            for y in range(1, self.size+1):
                y_row = '%s-0-%s' % (y, x_row.split('-')[-1])
                for z in range(1, self.size+1):
                    z_row = '%s-%s-0' % (y, z)
                    max_elems['%s.%s.%s' % (x_row, y_row, z_row)] = \
                        line_sum_x[1] + self.y[y_row] + self.z[z_row]
        result_list = self._get_sorted_list(max_elems)[0]
        self.result = result_list[0]
        self.result_sum = result_list[1]
