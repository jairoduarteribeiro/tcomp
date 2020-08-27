import unittest
from dfa import DFA


class A(DFA):
    def __init__(self):
        super().__init__(states={0, 1, 2}, alphabet={
            '0', '1'}, start_state=0, final_states={1})
        self._transition_table[(0, '0')] = 2
        self._transition_table[(0, '1')] = 0
        self._transition_table[(1, '0')] = 1
        self._transition_table[(1, '1')] = 1
        self._transition_table[(2, '0')] = 2
        self._transition_table[(2, '1')] = 1


class DFATestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = A()

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
