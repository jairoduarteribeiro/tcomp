from unittest import TestCase
from grammar.cfg import CFG


class CFGTestCase(TestCase):
    def test_replace_start_symbol(self):
        g1 = CFG(
            variables={'S', 'A', 'B'},
            terminals={'a', 'b'},
            productions={
                ('S', ('A', 'S', 'A')),
                ('S', ('a', 'B')),
                ('A', ('B', 'b')),
                ('B', ('b',)),
                ('B', ('',))
            },
            start_symbol='S'
        )
        self.assertEqual(g1._replace_start_symbol(), CFG(
            variables={'$0', 'S', 'A', 'B'},
            terminals={'a', 'b'},
            productions={
                ('$0', ('S',)),
                ('S', ('A', 'S', 'A')),
                ('S', ('a', 'B')),
                ('A', ('B', 'b')),
                ('B', ('b',)),
                ('B', ('',))
            },
            start_symbol='$0'
        ))

        g2 = CFG(
            variables={'S', 'A'},
            terminals={'a', 'b'},
            productions={
                ('S', ('A', 'B')),
                ('S', ('a',)),
                ('A', ('b',))
            },
            start_symbol='S'
        )
        self.assertEqual(g2._replace_start_symbol(), g2)

    def test_remove_epsilon(self):
        g1 = CFG(
            variables={'$0', 'S', 'A', 'B'},
            terminals={'a', 'b'},
            productions={
                ('$0', ('S',)),
                ('S', ('A', 'S', 'A')),
                ('S', ('a', 'B')),
                ('A', ('B',)),
                ('A', ('S',)),
                ('B', ('b',)),
                ('B', ('',))
            },
            start_symbol='$0'
        )
        self.assertEqual(g1._remove_epsilon(), CFG(
            variables={'$0', 'S', 'A', 'B'},
            terminals={'a', 'b'},
            productions={
                ('$0', ('S',)),
                ('S', ('A', 'S', 'A')),
                ('S', ('S', 'A')),
                ('S', ('A', 'S')),
                ('S', ('S',)),
                ('S', ('a', 'B')),
                ('S', ('a',)),
                ('A', ('B',)),
                ('A', ('S',)),
                ('B', ('b',))
            },
            start_symbol='$0'
        ))

        g2 = CFG(
            variables={'S', 'A', 'B'},
            terminals={'a', 'b'},
            productions={
                ('S', ('A', 'B')),
                ('A', ('a', 'A', 'A',)),
                ('A', ('',)),
                ('B', ('b', 'B', 'B')),
                ('B', ('',))
            },
            start_symbol='S'
        )
        self.assertEqual(g2._remove_epsilon(), CFG(
            variables={'S', 'A', 'B'},
            terminals={'a', 'b'},
            productions={
                ('S', ('A', 'B')),
                ('S', ('A',)),
                ('S', ('B',)),
                ('S', ('',)),
                ('A', ('a', 'A', 'A')),
                ('A', ('a', 'A')),
                ('A', ('a',)),
                ('B', ('b', 'B', 'B')),
                ('B', ('b', 'B',)),
                ('B', ('b',))
            },
            start_symbol='S'
        ))
