import unittest
import z12


class TestZ12(unittest.TestCase):

    def test_compare(self):
        self.assertEquals(z12.hanoi(2, 'A', 'B', 'C'), 'Przenieś krążek 1 z miejsca A do B\nPrzenieś krążek 2 z miejsca A do C\nPrzenieś krążek 1 z miejsca B do C')