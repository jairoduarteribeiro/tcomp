import unittest
from src.automaton.nfa import NFA


class A(NFA):
    def __init__(self):
        super().__init__(
            states={0, 1, 2, 3, 4, 5},
            alphabet={'0', '1', '2', '3', '4', '5',
                      '6', '7', '8', '9', '+', '-', '.'},
            start_state=0,
            final_states={5}
        )
        self.add_transition(0, '', {1})
        self.add_transition(0, '+', {1})
        self.add_transition(0, '-', {1})
        self.add_transition(1, '0', {1, 4})
        self.add_transition(1, '1', {1, 4})
        self.add_transition(1, '2', {1, 4})
        self.add_transition(1, '3', {1, 4})
        self.add_transition(1, '4', {1, 4})
        self.add_transition(1, '5', {1, 4})
        self.add_transition(1, '6', {1, 4})
        self.add_transition(1, '7', {1, 4})
        self.add_transition(1, '8', {1, 4})
        self.add_transition(1, '9', {1, 4})
        self.add_transition(1, '.', {2})
        self.add_transition(2, '0', {3})
        self.add_transition(2, '1', {3})
        self.add_transition(2, '2', {3})
        self.add_transition(2, '3', {3})
        self.add_transition(2, '4', {3})
        self.add_transition(2, '5', {3})
        self.add_transition(2, '6', {3})
        self.add_transition(2, '7', {3})
        self.add_transition(2, '8', {3})
        self.add_transition(2, '9', {3})
        self.add_transition(3, '', {5})
        self.add_transition(3, '0', {3})
        self.add_transition(3, '1', {3})
        self.add_transition(3, '2', {3})
        self.add_transition(3, '3', {3})
        self.add_transition(3, '4', {3})
        self.add_transition(3, '5', {3})
        self.add_transition(3, '6', {3})
        self.add_transition(3, '7', {3})
        self.add_transition(3, '8', {3})
        self.add_transition(3, '9', {3})
        self.add_transition(4, '.', {3})


class NFATestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = A()

    def test_e_close(self):
        self.assertEqual(self.a._e_close(0), frozenset({0, 1}))
        self.assertEqual(self.a._e_close(1), frozenset({1}))
        self.assertEqual(self.a._e_close(2), frozenset({2}))
        self.assertEqual(self.a._e_close(3), frozenset({3, 5}))
        self.assertEqual(self.a._e_close(4), frozenset({4}))
        self.assertEqual(self.a._e_close(5), frozenset({5}))
        self.assertEqual(self.a._e_close(
            frozenset({2, 3})), frozenset({2, 3, 5}))

    def test_transition_function(self):
        self.assertEqual(self.a._transition_function(0, ''), frozenset({1}))
        self.assertEqual(self.a._transition_function(0, '0'), frozenset())
        self.assertEqual(self.a._transition_function(0, '+'), frozenset({1}))
        self.assertEqual(self.a._transition_function(0, '.'), frozenset())
        self.assertEqual(self.a._transition_function(1, ''), frozenset())
        self.assertEqual(self.a._transition_function(
            1, '0'), frozenset({1, 4}))
        self.assertEqual(self.a._transition_function(1, '+'), frozenset())
        self.assertEqual(self.a._transition_function(1, '.'), frozenset({2}))
        self.assertEqual(self.a._transition_function(2, ''), frozenset())
        self.assertEqual(self.a._transition_function(2, '0'), frozenset({3}))
        self.assertEqual(self.a._transition_function(2, '+'), frozenset())
        self.assertEqual(self.a._transition_function(2, '.'), frozenset())
        self.assertEqual(self.a._transition_function(3, ''), frozenset({5}))
        self.assertEqual(self.a._transition_function(3, '0'), frozenset({3}))
        self.assertEqual(self.a._transition_function(3, '+'), frozenset())
        self.assertEqual(self.a._transition_function(3, '.'), frozenset())
        self.assertEqual(self.a._transition_function(4, ''), frozenset())
        self.assertEqual(self.a._transition_function(4, '0'), frozenset())
        self.assertEqual(self.a._transition_function(4, '+'), frozenset())
        self.assertEqual(self.a._transition_function(4, '.'), frozenset({3}))
        self.assertEqual(self.a._transition_function(5, ''), frozenset())
        self.assertEqual(self.a._transition_function(5, '0'), frozenset())
        self.assertEqual(self.a._transition_function(5, '+'), frozenset())
        self.assertEqual(self.a._transition_function(5, '.'), frozenset())

    def test_ext_transition_function(self):
        self.assertEqual(self.a._ext_transition_function(
            0, ''), frozenset({0, 1}))
        self.assertEqual(self.a._ext_transition_function(
            0, '5'), frozenset({1, 4}))
        self.assertEqual(self.a._ext_transition_function(
            0, '5.'), frozenset({2, 3, 5}))
        self.assertEqual(self.a._ext_transition_function(
            0, '5.6'), frozenset({3, 5}))
        self.assertEqual(self.a._ext_transition_function(
            0, '+'), frozenset({1}))
        self.assertEqual(self.a._ext_transition_function(
            0, '+5'), frozenset({1, 4}))
        self.assertEqual(self.a._ext_transition_function(
            0, '+5.'), frozenset({2, 3, 5}))
        self.assertEqual(self.a._ext_transition_function(
            0, '+5.6'), frozenset({3, 5}))

    def test_accept(self):
        self.assertTrue(self.a.accept('0.'))
        self.assertTrue(self.a.accept('000.'))
        self.assertTrue(self.a.accept('.0'))
        self.assertTrue(self.a.accept('.000'))
        self.assertTrue(self.a.accept('+0.'))
        self.assertTrue(self.a.accept('+000.'))
        self.assertTrue(self.a.accept('+.0'))
        self.assertTrue(self.a.accept('+.000'))
        self.assertTrue(self.a.accept('0.0'))
        self.assertTrue(self.a.accept('000.0'))
        self.assertTrue(self.a.accept('0.000'))
        self.assertTrue(self.a.accept('000.000'))
        self.assertTrue(self.a.accept('+0.0'))
        self.assertTrue(self.a.accept('+000.0'))
        self.assertTrue(self.a.accept('+0.000'))
        self.assertTrue(self.a.accept('+000.000'))
        self.assertFalse(self.a.accept(''))
        self.assertFalse(self.a.accept('0'))
        self.assertFalse(self.a.accept('.'))
        self.assertFalse(self.a.accept('..0'))
        self.assertFalse(self.a.accept('..000'))
        self.assertFalse(self.a.accept('0..'))
        self.assertFalse(self.a.accept('000..'))
        self.assertFalse(self.a.accept('0..0'))
        self.assertFalse(self.a.accept('000..0'))
        self.assertFalse(self.a.accept('0..000'))
        self.assertFalse(self.a.accept('000..000'))
        self.assertFalse(self.a.accept('+'))
        self.assertFalse(self.a.accept('+0'))
        self.assertFalse(self.a.accept('+.'))
        self.assertFalse(self.a.accept('+..0'))
        self.assertFalse(self.a.accept('+..000'))
        self.assertFalse(self.a.accept('+0..'))
        self.assertFalse(self.a.accept('+000..'))
        self.assertFalse(self.a.accept('+0..0'))
        self.assertFalse(self.a.accept('+000..0'))
        self.assertFalse(self.a.accept('+0..000'))
        self.assertFalse(self.a.accept('+000..000'))

    def test_convert_to_dfa(self):
        a = self.a.convert_to_dfa()
        self.assertTrue(a.accept('0.'))
        self.assertTrue(a.accept('000.'))
        self.assertTrue(a.accept('.0'))
        self.assertTrue(a.accept('.000'))
        self.assertTrue(a.accept('+0.'))
        self.assertTrue(a.accept('+000.'))
        self.assertTrue(a.accept('+.0'))
        self.assertTrue(a.accept('+.000'))
        self.assertTrue(a.accept('0.0'))
        self.assertTrue(a.accept('000.0'))
        self.assertTrue(a.accept('0.000'))
        self.assertTrue(a.accept('000.000'))
        self.assertTrue(a.accept('+0.0'))
        self.assertTrue(a.accept('+000.0'))
        self.assertTrue(a.accept('+0.000'))
        self.assertTrue(a.accept('+000.000'))
        self.assertFalse(a.accept(''))
        self.assertFalse(a.accept('0'))
        self.assertFalse(a.accept('.'))
        self.assertFalse(a.accept('..0'))
        self.assertFalse(a.accept('..000'))
        self.assertFalse(a.accept('0..'))
        self.assertFalse(a.accept('000..'))
        self.assertFalse(a.accept('0..0'))
        self.assertFalse(a.accept('000..0'))
        self.assertFalse(a.accept('0..000'))
        self.assertFalse(a.accept('000..000'))
        self.assertFalse(a.accept('+'))
        self.assertFalse(a.accept('+0'))
        self.assertFalse(a.accept('+.'))
        self.assertFalse(a.accept('+..0'))
        self.assertFalse(a.accept('+..000'))
        self.assertFalse(a.accept('+0..'))
        self.assertFalse(a.accept('+000..'))
        self.assertFalse(a.accept('+0..0'))
        self.assertFalse(a.accept('+000..0'))
        self.assertFalse(a.accept('+0..000'))
        self.assertFalse(a.accept('+000..000'))


if __name__ == '__main__':
    unittest.main()
