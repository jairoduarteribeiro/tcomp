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

    def test_convert_to_dfa(self):
        dawg = DAWG({'aba +', 'baa +', 'b +', 'a', 'bab', 'aaa'})
        dfa = dawg.convert_to_dfa()
        self.assertEqual(dfa._states, frozenset({
            frozenset(),
            frozenset({frozenset({'aba', 'baa', 'b'})}),
            frozenset({frozenset({'ba'}), frozenset({'', 'aa'}), frozenset({''})}),
            frozenset({frozenset({'ba'})}),
            frozenset({frozenset({'a'})}),
            frozenset({frozenset({''})})
        }))
        self.assertEqual(dfa._alphabet, frozenset({'a', 'b'}))
        self.assertEqual(dfa._start_state, frozenset({frozenset({'aba', 'baa', 'b'})}))
        self.assertEqual(dfa._final_states, frozenset({
            frozenset({frozenset({'ba'}), frozenset({'', 'aa'}), frozenset({''})}),
            frozenset({frozenset({''})})
        }))
        self.assertEqual(dfa._transition_table, {
            (frozenset({frozenset({'aba', 'baa', 'b'})}), 'a'):
                frozenset({frozenset({'ba'})}),
            (frozenset({frozenset({'aba', 'baa', 'b'})}), 'b'):
                frozenset({frozenset({'ba'}), frozenset({'', 'aa'}), frozenset({''})}),
            (frozenset({frozenset({'ba'})}), 'a'):
                frozenset(),
            (frozenset({frozenset({'ba'})}), 'b'):
                frozenset({frozenset({'a'})}),
            (frozenset({frozenset({'ba'}), frozenset({'', 'aa'}), frozenset({''})}), 'a'):
                frozenset({frozenset({'a'})}),
            (frozenset({frozenset({'ba'}), frozenset({'', 'aa'}), frozenset({''})}), 'b'):
                frozenset({frozenset({'a'})}),
            (frozenset({frozenset({'a'})}), 'a'):
                frozenset({frozenset({''})}),
            (frozenset({frozenset({'a'})}), 'b'):
                frozenset(),
            (frozenset({frozenset({''})}), 'a'):
                frozenset(),
            (frozenset({frozenset({''})}), 'b'):
                frozenset(),
            (frozenset(), 'a'):
                frozenset(),
            (frozenset(), 'b'):
                frozenset(),
        })
