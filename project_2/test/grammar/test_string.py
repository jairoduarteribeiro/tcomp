from unittest import TestCase
from src.grammar.string import String


class StringTestCase(TestCase):
    def test_equals(self):
        s1 = String(['a'])
        s2 = String(['a'])
        self.assertTrue(s1 == s2)
