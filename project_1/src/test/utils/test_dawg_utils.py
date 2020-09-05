import unittest
from src.utils.dawg_utils import DAWGUtils


class DAWGUtilsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.labels = {
            (frozenset({'b', 'baa', 'aba'}), frozenset({'ba'})): frozenset({'a'}),
            (frozenset({'b', 'baa', 'aba'}), frozenset({''})): frozenset({'b'}),
            (frozenset({'b', 'baa', 'aba'}), frozenset({'', 'aa'})): frozenset({'b'}),
            (frozenset({'ba'}), frozenset({'a'})): frozenset({'b'}),
            (frozenset({'', 'aa'}), frozenset({'a'})): frozenset({'a'}),
            (frozenset({'a'}), frozenset({''})): frozenset({'a'})
        }
        cls.potency = {
            (frozenset({'aba', 'baa', 'b'}), frozenset({'ba'})): 1,
            (frozenset({'aba', 'baa', 'b'}), frozenset({'', 'aa'})): 1,
            (frozenset({'aba', 'baa', 'b'}), frozenset({''})): 1,
            (frozenset({'ba'}), frozenset({'a'})): 1,
            (frozenset({'', 'aa'}), frozenset({'a'})): 1,
            (frozenset({'a'}), frozenset({''})): 1
        }

    def test_build_sample(self):
        self.assertEqual(
            DAWGUtils.build_sample({'aba +', 'baa +', 'b +', 'a', 'bab', 'aaa'}),
            {'+': frozenset({'aba', 'baa', 'b'}), '-': frozenset({'a', 'bab', 'aaa'})})

    def test_prefixes(self):
        self.assertEqual(DAWGUtils.prefixes('abc'), frozenset({'', 'a', 'ab', 'abc'}))
        self.assertEqual(
            DAWGUtils.prefixes(frozenset({'aba', 'baa', 'b'})),
            frozenset({'', 'a', 'ab', 'aba', 'b', 'ba', 'baa'})
        )

    def test_left_quotients(self):
        self.assertEqual(
            DAWGUtils.left_quotients('', frozenset({'aba', 'baa', 'b'})),
            frozenset({'aba', 'baa', 'b'})
        )
        self.assertEqual(
            DAWGUtils.left_quotients('a', frozenset({'aba', 'baa', 'b'})),
            frozenset({'ba'})
        )

    def test_v_a_l(self):
        v_a_l = DAWGUtils.v_a_l(frozenset({'aba', 'baa', 'b'}))
        self.assertEqual(
            v_a_l('v'),
            frozenset({
                frozenset({'aba', 'baa', 'b'}),
                frozenset({'ba'}),
                frozenset({'a'}),
                frozenset({'aa', ''}),
                frozenset({''})
            })
        )
        self.assertEqual(
            v_a_l('a'),
            frozenset({
                (frozenset({'aba', 'baa', 'b'}), frozenset({''})),
                (frozenset({'aba', 'baa', 'b'}), frozenset({'aa', ''})),
                (frozenset({'aba', 'baa', 'b'}), frozenset({'ba'})),
                (frozenset({'ba'}), frozenset({'a'})),
                (frozenset({'aa', ''}), frozenset({'a'})),
                (frozenset({'a'}), frozenset({''}))
            })
        )
        self.assertEqual(
            v_a_l('l'),
            self.labels
        )

    def test_potency(self):
        self.assertEqual(
            DAWGUtils.potency({(1, 2), (1, 3), (1, 5), (2, 4), (3, 4), (4, 5)}, 1, 5),
            {(1, 2): 1, (1, 3): 1, (1, 5): 1, (2, 4): 1, (3, 4): 1, (4, 5): 1}
        )
        self.assertEqual(
            DAWGUtils.potency({(1, 2), (2, 3), (2, 4), (3, 4)}, 1, 4),
            {(1, 2): 2, (2, 3): 1, (2, 4): 1, (3, 4): 1}
        )

    def test_transition(self):
        self.assertEqual(
            DAWGUtils.transition(frozenset({'aba', 'baa', 'b'}), 'a', self.labels),
            frozenset({frozenset({'ba'})})
        )
        self.assertEqual(
            DAWGUtils.transition(frozenset({'aba', 'baa', 'b'}), 'b', self.labels),
            frozenset({frozenset({'', 'aa'}), frozenset({''})})
        )
        self.assertEqual(
            DAWGUtils.transition(frozenset({'aba', 'baa', 'b'}), 'ab', self.labels),
            frozenset({frozenset({'a'})})
        )
        self.assertEqual(
            DAWGUtils.transition(frozenset({'aba', 'baa', 'b'}), 'ba', self.labels),
            frozenset({frozenset({'a'})})
        )
        self.assertEqual(
            DAWGUtils.transition(frozenset({'aba', 'baa', 'b'}), 'aba', self.labels),
            frozenset({frozenset({''})})
        )
        self.assertEqual(
            DAWGUtils.transition(frozenset({'aba', 'baa', 'b'}), 'baa', self.labels),
            frozenset({frozenset({''})})
        )

    def test_build_alphabet(self):
        self.assertEqual(
            DAWGUtils.build_alphabet(
                frozenset({'aba', 'baa', 'b'}),
                frozenset({'a', 'bab', 'aaa'})),
            frozenset({'a', 'b'})
        )
        self.assertEqual(
            DAWGUtils.build_alphabet(
                frozenset({'ab', 'bacaa', 'c'}),
                frozenset({'a', 'bab', 'aada'})),
            frozenset({'a', 'b', 'c', 'd'})
        )

    def test_extend(self):
        alphabet = frozenset({'a', 'b'})
        s_neg = frozenset({'a', 'bab', 'aaa'})
        s = frozenset({'aba', 'baa', 'b'})
        t = frozenset({''})
        self.assertEqual(
            DAWGUtils.extend(self.labels, self.potency, alphabet, s_neg, s, t), {
                (frozenset({'b', 'baa', 'aba'}), frozenset({'ba'})): frozenset({'a', 'b'}),
                (frozenset({'b', 'baa', 'aba'}), frozenset({''})): frozenset({'b'}),
                (frozenset({'b', 'baa', 'aba'}), frozenset({'', 'aa'})): frozenset({'b'}),
                (frozenset({'ba'}), frozenset({'a'})): frozenset({'b'}),
                (frozenset({'', 'aa'}), frozenset({'a'})): frozenset({'a', 'b'}),
                (frozenset({'a'}), frozenset({''})): frozenset({'a'})
            }
        )
