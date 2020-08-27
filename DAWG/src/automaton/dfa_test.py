import unittest
from dfa import DFA


class A(DFA):
    def __init__(self):
        super().__init__(
            states={0, 1, 2},
            alphabet={'0', '1'},
            start_state=0,
            final_states={1}
        )
        self.add_transition(0, '0', 2)
        self.add_transition(0, '1', 0)
        self.add_transition(1, '0', 1)
        self.add_transition(1, '1', 1)
        self.add_transition(2, '0', 2)
        self.add_transition(2, '1', 1)


class DFATestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = A()

    def test_transition_function(self):
        self.assertEqual(self.a._transition_function(0, '0'), 2)
        self.assertEqual(self.a._transition_function(0, '1'), 0)
        self.assertEqual(self.a._transition_function(1, '0'), 1)
        self.assertEqual(self.a._transition_function(1, '1'), 1)
        self.assertEqual(self.a._transition_function(2, '0'), 2)
        self.assertEqual(self.a._transition_function(2, '1'), 1)

    def test_ext_transition_function(self):
        self.assertEqual(self.a._ext_transition_function(0, ''), 0)
        self.assertEqual(self.a._ext_transition_function(0, '0'), 2)
        self.assertEqual(self.a._ext_transition_function(0, '1'), 0)
        self.assertEqual(self.a._ext_transition_function(0, '01'), 1)
        self.assertEqual(self.a._ext_transition_function(0, '11101'), 1)
        self.assertEqual(
            self.a._ext_transition_function(0, '11100001'), 1)
        self.assertEqual(
            self.a._ext_transition_function(0, '11100001000'), 1)
        self.assertEqual(
            self.a._ext_transition_function(0, '11100001111'), 1)
        self.assertEqual(self.a._ext_transition_function(0, '111'), 0)
        self.assertEqual(self.a._ext_transition_function(0, '1110'), 2)
        self.assertEqual(self.a._ext_transition_function(0, '1110000'), 2)

        self.assertEqual(self.a._ext_transition_function(1, ''), 1)
        self.assertEqual(self.a._ext_transition_function(1, '0'), 1)
        self.assertEqual(self.a._ext_transition_function(1, '1'), 1)
        self.assertEqual(self.a._ext_transition_function(1, '01'), 1)
        self.assertEqual(self.a._ext_transition_function(1, '11101'), 1)
        self.assertEqual(
            self.a._ext_transition_function(1, '11100001'), 1)
        self.assertEqual(
            self.a._ext_transition_function(1, '11100001000'), 1)
        self.assertEqual(
            self.a._ext_transition_function(1, '11100001111'), 1)
        self.assertEqual(self.a._ext_transition_function(1, '111'), 1)
        self.assertEqual(self.a._ext_transition_function(1, '1110'), 1)
        self.assertEqual(self.a._ext_transition_function(1, '1110000'), 1)

        self.assertEqual(self.a._ext_transition_function(2, ''), 2)
        self.assertEqual(self.a._ext_transition_function(2, '0'), 2)
        self.assertEqual(self.a._ext_transition_function(2, '1'), 1)
        self.assertEqual(self.a._ext_transition_function(2, '01'), 1)
        self.assertEqual(self.a._ext_transition_function(2, '11101'), 1)
        self.assertEqual(
            self.a._ext_transition_function(2, '11100001'), 1)
        self.assertEqual(
            self.a._ext_transition_function(2, '11100001000'), 1)
        self.assertEqual(
            self.a._ext_transition_function(2, '11100001111'), 1)
        self.assertEqual(self.a._ext_transition_function(2, '111'), 1)
        self.assertEqual(self.a._ext_transition_function(2, '1110'), 1)
        self.assertEqual(self.a._ext_transition_function(2, '1110000'), 1)

    def test_accept(self):
        self.assertTrue(self.a.accept('01'))
        self.assertTrue(self.a.accept('11101'))
        self.assertTrue(self.a.accept('11100001'))
        self.assertTrue(self.a.accept('11100001000'))
        self.assertTrue(self.a.accept('11100001111'))
        self.assertFalse(self.a.accept(''))
        self.assertFalse(self.a.accept('111'))
        self.assertFalse(self.a.accept('1110'))
        self.assertFalse(self.a.accept('1110000'))


if __name__ == '__main__':
    unittest.main()
