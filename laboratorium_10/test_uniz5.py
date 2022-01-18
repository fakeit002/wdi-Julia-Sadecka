import unittest
import z5


class TestZ5(unittest.TestCase):

    def setUp(self):
        self.matrix_1 = [[2, 1], [3, 4]]
        self.matrix_2 = [[4, 5], [1, 2]]
        self.matrix_3 = [[2, 4, 1], [2, 1, 3]]
        self.matrix_4 = [[8, 5, 2], [3, 2, 9]]
        self.matrix_5 = [[2, 0], [2, 4], [1, 9]]
        self.matrix_6 = [[1, 8], [5, 4], [6, 7]]

    def test_sum(self):
        self.assertEquals(z5.sum(self.matrix_1, self.matrix_2), '[[6, 6], [4, 6]]')
        self.assertEquals(z5.sum(self.matrix_3, self.matrix_4), '[[10, 9, 3], [5, 3, 12]]')
        self.assertEquals(z5.sum(self.matrix_5, self.matrix_6), '[[3, 8], [7, 8], [7, 16]]')

    def test_mult(self):
        self.assertEquals(z5.mult(self.matrix_1, self.matrix_2), '[[9, 12], [16, 23]]')
        self.assertEquals(z5.mult(self.matrix_3, self.matrix_5), '[[13, 25], [9, 31]]')
        self.assertEquals(z5.mult(self.matrix_6, self.matrix_1), '[[26, 33], [22, 21], [33, 34]]')

    def test_sub(self):
        self.assertEquals(z5.sub(self.matrix_1, self.matrix_2), '[[-2, -4], [2, 2]]')
        self.assertEquals(z5.sub(self.matrix_3, self.matrix_4), '[[-6, -1, -1], [-1, -1, -6]]')
        self.assertEquals(z5.sub(self.matrix_5, self.matrix_6), '[[1, -8], [-3, 0], [-5, 2]]')
