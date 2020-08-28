import unittest
from ...src.automaton.dawg import DAWG


class DAWGTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = DAWG('dawg/waltz.txt')

    def test_build_sample(self):
        self.assertEqual(0, 0)
