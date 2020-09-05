import unittest
from src.automaton.dawg import DAWG


class DAWGTestCase(unittest.TestCase):
    def test_build(self):
        dawg = DAWG({'aba +', 'baa +', 'b +', 'a', 'bab', 'aaa'})
        self.assertEqual(
            dawg._states,
            frozenset({
                frozenset({'aba', 'baa', 'b'}),
                frozenset({'ba'}),
                frozenset({'a'}),
                frozenset({'aa', ''}),
                frozenset({''})
            })
        )
        self.assertEqual(dawg._alphabet, frozenset({'a', 'b'}))
        self.assertEqual(dawg._start_state, frozenset({'aba', 'baa', 'b'}))
        self.assertEqual(dawg._final_states, frozenset({frozenset({''})}))
        self.assertEqual(
            dawg._transition_table,
            {
                (frozenset({'aba', 'baa', 'b'}), 'a'): {
                    frozenset({'ba'})
                },
                (frozenset({'aba', 'baa', 'b'}), 'b'): {
                    frozenset({''}),
                    frozenset({'ba'}),
                    frozenset({'', 'aa'})
                },
                (frozenset({'ba'}), 'b'): {
                    frozenset({'a'})
                },
                (frozenset({'', 'aa'}), 'a'): {
                    frozenset({'a'})
                },
                (frozenset({'', 'aa'}), 'b'): {
                    frozenset({'a'})
                },
                (frozenset({'a'}), 'a'): {
                    frozenset({''})
                },
            }
        )
