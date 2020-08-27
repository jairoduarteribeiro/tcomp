import unittest
from nfa import NFA


class A(NFA):
    def __init__(self):
        super().__init__(
            {0, 1, 2, 3, 4, 5},
            {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.'},
            0,
            {5}
        )
        self._transition_table[(0, '')] = {1}
        self._transition_table[(0, '+')] = {1}
        self._transition_table[(0, '-')] = {1}

        self._transition_table[(1, '0')] = {1, 4}
        self._transition_table[(1, '1')] = {1, 4}
        self._transition_table[(1, '2')] = {1, 4}
        self._transition_table[(1, '3')] = {1, 4}
        self._transition_table[(1, '4')] = {1, 4}
        self._transition_table[(1, '5')] = {1, 4}
        self._transition_table[(1, '6')] = {1, 4}
        self._transition_table[(1, '7')] = {1, 4}
        self._transition_table[(1, '8')] = {1, 4}
        self._transition_table[(1, '9')] = {1, 4}
        self._transition_table[(1, '.')] = {2}

        self._transition_table[(2, '0')] = {3}
        self._transition_table[(2, '1')] = {3}
        self._transition_table[(2, '2')] = {3}
        self._transition_table[(2, '3')] = {3}
        self._transition_table[(2, '4')] = {3}
        self._transition_table[(2, '5')] = {3}
        self._transition_table[(2, '6')] = {3}
        self._transition_table[(2, '7')] = {3}
        self._transition_table[(2, '8')] = {3}
        self._transition_table[(2, '9')] = {3}

        self._transition_table[(3, '')] = {5}
        self._transition_table[(3, '0')] = {3}
        self._transition_table[(3, '1')] = {3}
        self._transition_table[(3, '2')] = {3}
        self._transition_table[(3, '3')] = {3}
        self._transition_table[(3, '4')] = {3}
        self._transition_table[(3, '5')] = {3}
        self._transition_table[(3, '6')] = {3}
        self._transition_table[(3, '7')] = {3}
        self._transition_table[(3, '8')] = {3}
        self._transition_table[(3, '9')] = {3}

        self._transition_table[(4, '.')] = {3}


class NFATestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = A()

    def test_eclose(self):
        self.assertEqual(self.a._eclose(0), {0, 1})
        self.assertEqual(self.a._eclose(1), {1})
        self.assertEqual(self.a._eclose(2), {2})
        self.assertEqual(self.a._eclose(3), {3, 5})
        self.assertEqual(self.a._eclose(4), {4})
        self.assertEqual(self.a._eclose(5), {5})
        self.assertEqual(self.a._eclose({2, 3}), {2, 3, 5})

    def test_transition_function(self):
        self.assertEqual(self.a._transition_function(0, ''), {1})
        self.assertEqual(self.a._transition_function(0, '0'), set())
        self.assertEqual(self.a._transition_function(0, '+'), {1})
        self.assertEqual(self.a._transition_function(0, '.'), set())
        self.assertEqual(self.a._transition_function(1, ''), set())
        self.assertEqual(self.a._transition_function(1, '0'), {1, 4})
        self.assertEqual(self.a._transition_function(1, '+'), set())
        self.assertEqual(self.a._transition_function(1, '.'), {2})
        self.assertEqual(self.a._transition_function(2, ''), set())
        self.assertEqual(self.a._transition_function(2, '0'), {3})
        self.assertEqual(self.a._transition_function(2, '+'), set())
        self.assertEqual(self.a._transition_function(2, '.'), set())
        self.assertEqual(self.a._transition_function(3, ''), {5})
        self.assertEqual(self.a._transition_function(3, '0'), {3})
        self.assertEqual(self.a._transition_function(3, '+'), set())
        self.assertEqual(self.a._transition_function(3, '.'), set())
        self.assertEqual(self.a._transition_function(4, ''), set())
        self.assertEqual(self.a._transition_function(4, '0'), set())
        self.assertEqual(self.a._transition_function(4, '+'), set())
        self.assertEqual(self.a._transition_function(4, '.'), {3})
        self.assertEqual(self.a._transition_function(5, ''), set())
        self.assertEqual(self.a._transition_function(5, '0'), set())
        self.assertEqual(self.a._transition_function(5, '+'), set())
        self.assertEqual(self.a._transition_function(5, '.'), set())

    def test_ext_transition_function(self):
        self.assertEqual(self.a._ext_transition_function(0, ''), {0, 1})
        self.assertEqual(self.a._ext_transition_function(0, '5'), {1, 4})
        self.assertEqual(self.a._ext_transition_function(0, '5.'), {2, 3, 5})
        self.assertEqual(self.a._ext_transition_function(0, '5.6'), {3, 5})
        self.assertEqual(self.a._ext_transition_function(0, '+'), {1})
        self.assertEqual(self.a._ext_transition_function(0, '+5'), {1, 4})
        self.assertEqual(self.a._ext_transition_function(0, '+5.'), {2, 3, 5})
        self.assertEqual(self.a._ext_transition_function(0, '+5.6'), {3, 5})

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


if __name__ == '__main__':
    unittest.main()
