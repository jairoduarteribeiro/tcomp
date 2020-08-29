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

    def test_potency(self):
        self.assertEqual(self.a._potency({(1, 2), (1, 3), (1, 5), (2, 4), (3, 4),
                                          (4, 5)}, 1, 5),
                         {(1, 2): 1, (1, 3): 1, (1, 5): 1, (2, 4): 1, (3, 4): 1,
                          (4, 5): 1})
        self.assertEqual(self.a._potency({(1, 2), (2, 3), (2, 4), (3, 4)}, 1, 4),
                         {(1, 2): 2,
                          (2, 3): 1, (2, 4): 1, (3, 4): 1})

    def test_transition(self):
        self.assertEqual(self.a._transition(3, 'aa',
                                            {(1, 2):
                                                 frozenset({'a'}),
                                             (1, 5):
                                                 frozenset({'b'}),
                                             (
                                                 1, 3):
                                                 frozenset({'b'}),
                                             (2, 4):
                                                 frozenset({'b'}),
                                             (3, 4):
                                                 frozenset({'a'}),
                                             (4, 5):
                                                 frozenset({'a'})}), frozenset({5}))
        self.assertEqual(self.a._transition(1, 'b', {(1, 2):
                                                 frozenset({'a'}),
                                             (1, 5):
                                                 frozenset({'b'}),
                                             (
                                                 1, 3):
                                                 frozenset({'b'}),
                                             (2, 4):
                                                 frozenset({'b'}),
                                             (3, 4):
                                                 frozenset({'a'}),
                                             (4, 5):
                                                 frozenset({'a'})}), frozenset({3, 5}))
