import unittest
from src.automaton.dawg import DAWG


class DAWGTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = DAWG()

    def test_build_sample(self):
        self.assertEqual(self.a._build_sample({'aba +', 'baa +', 'b +', 'a',
                                               'bab', 'aaa'}),
                         {'+': frozenset({'aba', 'baa', 'b'}), '-': frozenset({
                             'a', 'bab', 'aaa'
                         })})

    def test_p(self):
        self.assertEqual(self.a._p('abc'), frozenset({'', 'a', 'ab', 'abc'}))
        self.assertEqual(self.a._p(frozenset({'aba', 'baa', 'b'})), frozenset({'', 'a', 'ab',
                                                                               'aba', 'b', 'ba',
                                                                               'baa'}))
