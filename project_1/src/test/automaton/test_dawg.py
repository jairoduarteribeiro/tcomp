import unittest
import os
from src.automaton.dawg import DAWG


class DAWGTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = DAWG()

    def test_build_sample(self):
        dataset = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sample.txt')
        self.assertEqual(DAWG.build_sample(dataset),
                         {'+': frozenset({'aba', 'baa', 'b'}), '-': frozenset({
                             'a', 'bab', 'aaa'
                         })})
