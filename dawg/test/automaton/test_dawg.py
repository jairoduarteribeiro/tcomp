import unittest
from ...src.automaton.dawg import DAWG


class DAWGTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = DAWG()

    def test_build_sample(self):
        sample = self.a._build_sample('dawg/test/sample.txt')
        self.assertEqual(sample, {
                         '+': frozenset({'aba', 'baa', 'b'}),
                         '-': frozenset({'a', 'bab', 'aaa'})})
