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

    def test_left_quotients(self):
        self.assertEqual(self.a._left_quotients('', frozenset({'aba', 'baa', 'b'})),
                         frozenset({'aba', 'baa', 'b'}))
        self.assertEqual(self.a._left_quotients('a', frozenset({'aba', 'baa', 'b'})), frozenset({
            'ba'}))

    def test_v(self):
        self.assertEqual(self.a._v(frozenset({'aba', 'baa', 'b'})),
                         {'': frozenset({'b', 'baa', 'aba'}),
                          'a': frozenset({'ba'}),
                          'ab': frozenset({'a'}),
                          'aba': frozenset({''}),
                          'b': frozenset({'', 'aa'}),
                          'ba': frozenset({'a'}),
                          'baa': frozenset({''})})

    def test_l(self):
        self.assertEqual(self.a._l({'': frozenset({'b', 'baa', 'aba'}),
                                    'a': frozenset({'ba'}),
                                    'ab': frozenset({'a'}),
                                    'aba': frozenset({''}),
                                    'b': frozenset({'', 'aa'}),
                                    'ba': frozenset({'a'}),
                                    'baa': frozenset({''})}),
                         {(frozenset({'b', 'baa', 'aba'}), frozenset({'ba'})):
                              frozenset({'a'}), (frozenset({'b', 'baa', 'aba'}), frozenset({''})):
                              frozenset({'b'}),
                          (frozenset({'b', 'baa', 'aba'}), frozenset({'', 'aa'})):
                              frozenset({'b'}), (frozenset({'ba'}), frozenset({'a'})):
                              frozenset({'b'}), (frozenset({'', 'aa'}), frozenset({'a'})):
                              frozenset({'a'}), (frozenset({'a'}), frozenset({''})):
                              frozenset({'a'})})
