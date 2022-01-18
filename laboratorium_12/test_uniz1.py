import unittest
import z1


class TestZ1(unittest.TestCase):

    def test_reduce(self):
        self.assertEquals(z1.red2([2, 4]), [1, 2])
