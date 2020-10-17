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
