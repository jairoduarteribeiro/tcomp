from src.automaton.dfa import DFA
from src.utils.set_utils import SetUtils


class NFA(DFA):
    def __init__(self, states, alphabet, start_state, final_states, transition_table):
        super().__init__(states, alphabet, start_state, final_states, transition_table)

    def _e_close(self, state):
        epsilon_transitions = self._transition_function(state, '')
        return frozenset({state}).union(self._e_close_set(epsilon_transitions))

    def _e_close_set(self, states):
        return SetUtils.union_all_fn(states, self._e_close)

    def _transition_function(self, state, symbol):
        try:
            return frozenset(super()._transition_function(state, symbol))
        except KeyError:
            return frozenset()

    def _ext_transition_function(self, state, string):
        if not string:
            return self._e_close(state)
        else:
            x = string[0:-1]
            a = string[-1]

            transitions = self._ext_transition_function(state, x)
            transitions = SetUtils.union_all_fn(transitions, self._transition_function, a)
            return SetUtils.union_all_fn(transitions, self._e_close)

    def accept(self, string):
        result = self._ext_transition_function(self._start_state, string)
        return bool(result.intersection(self._final_states))

    def convert_to_dfa(self):
        dfa_states = SetUtils.power_set(self._states)
        dfa_alphabet = self._alphabet
        dfa_start_state = self._e_close(self._start_state)
        dfa_final_states = filter(
            lambda states: states.intersection(self._final_states), dfa_states
        )
        dfa_transition_table = dict()

        for symbol in self._alphabet:
            for state in dfa_states:
                r = SetUtils.union_all_fn(state, self._transition_function, symbol)
                dfa_transition_table[(state, symbol)] = self._e_close_set(r)

        return DFA(
            states=dfa_states,
            alphabet=dfa_alphabet,
            start_state=dfa_start_state,
            final_states=dfa_final_states,
            transition_table=dfa_transition_table
        )
