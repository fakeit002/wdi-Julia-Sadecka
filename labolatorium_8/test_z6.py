import unittest
import z6


class TestZ6(unittest.TestCase):

    def test_compare(self):
        self.assertEquals(z6.compare([1, 1, 2, 1, 2, 3, 4]), 2)
        self.assertEquals(z6.compare([67, 34, 2, 5, 11, 10, 1, 5, 8, 10, 13, 14, 9, 90]), 6)
        self.assertEquals(z6.compare([1, 2, 3, 2, 1, 5, 6]), 0)
        self.assertEquals(z6.compare([1, 2, 3, 3, 4, 5, 1, 7, 8, 9, 15]), 5)

        self.assertRaises(ValueError, z6.compare, 'asd')
