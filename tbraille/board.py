import math


class Cell:

    def __init__(self):
        self.value = 0

    @staticmethod
    def _get_bit(x, y):
        '''
        03
        14
        25
        67
        '''
        if y < 3:
            return x * 3 + y
        return y * 2 + x

    def __getitem__(self, tup):
        x, y = tup
        assert 0 <= x < 2 and 0 <= y < 4
        if self.value & 1 << self._get_bit(x, y):
            return 1
        return 0

    def __setitem__(self, tup, value):
        x, y = tup
        assert 0 <= x < 2 and 0 <= y < 4
        if value:
            self.value |= 1 << self._get_bit(x, y)
        else:
            self.value &= ~(1 << self._get_bit(x, y))

    def __str__(self):
        return chr(0x2800 + self.value)


class Board:

    def __init__(self, x, y):
        self.cols = math.ceil(x / 2)
        self.rows = math.ceil(y / 4)

        self.cells = [Cell() for i in range(self.cols * self.rows)]

    def __getitem__(self, tup):
        x, y = tup
        x1, x2 = divmod(x, 2)
        y1, y2 = divmod(y, 4)

        cell = self.cells[y1 * self.cols + x1]
        return cell[x2, y2]

    def __setitem__(self, tup, value):
        x, y = tup
        x1, x2 = divmod(x, 2)
        y1, y2 = divmod(y, 4)

        cell = self.cells[y1 * self.cols + x1]
        cell[x2, y2] = value

    def __str__(self):
        return '\n'.join(
            ''.join(
                str(self.cells[y * self.cols + x])
                for x in range(self.cols)
            ).rstrip(chr(0x2800))
            for y in range(self.rows)
        )
