import unittest
from ...src.utils.set_utils import SetUtils


class SetUtilsTestCase(unittest.TestCase):
    def test_union_all_fn(self):
        self.assertEqual(SetUtils.union_all_fn(
            {1, 2, 3}, lambda x: {x, x % 2}), frozenset({0, 1, 2, 3}))

    def test_power_set(self):
        self.assertEqual(SetUtils.power_set(
            {1, 2, 3}), frozenset([frozenset(), frozenset({1}), frozenset({2}),
                                   frozenset({3}), frozenset({1, 2}),
                                   frozenset({1, 3}), frozenset({2, 3}),
                                   frozenset({1, 2, 3})]))
        self.assertEqual(SetUtils.power_set(set()), frozenset([frozenset()]))
