from src.automaton.dfa import DFA
from src.utils.set_utils import SetUtils


class NFA(DFA):
    def __init__(self, states, alphabet, start_state, final_states,
                 transition_table=None):
        super().__init__(states, alphabet, start_state, final_states,
                         transition_table)

    def _e_close(self, st):
        if isinstance(st, frozenset):
            return SetUtils.union_all_fn(st, self._e_close)
        else:
            epsilon_transitions = self._transition_function(st, '')
            return frozenset({st}).union(self._e_close(epsilon_transitions))

    def _transition_function(self, state, symbol):
        try:
            return super()._transition_function(state, symbol)
        except KeyError:
            return frozenset()

    def _ext_transition_function(self, state, string):
        if not string:
            return self._e_close(state)
        else:
            x = string[0:-1]
            a = string[-1]

            transitions = self._ext_transition_function(state, x)
            transitions = SetUtils.union_all_fn(
                transitions, self._transition_function, a)
            return SetUtils.union_all_fn(transitions, self._e_close)

    def add_transition(self, state_before, symbol, state_after):
        self._transition_table[(state_before, symbol)] = \
            self._transition_function(state_before, symbol).union(frozenset(state_after))

    def accept(self, string):
        result = self._ext_transition_function(self._start_state, string)
        return bool(result.intersection(self._final_states))

    def convert_to_dfa(self):
        dfa_states = SetUtils.power_set(self._states)
        dfa_start_state = self._e_close(self._start_state)
        dfa_final_states = filter(lambda states: len(
            states.intersection(self._final_states)) > 0, dfa_states)
        dfa = DFA(dfa_states, self._alphabet,
                  dfa_start_state, dfa_final_states)

        for symbol in self._alphabet:
            for s in dfa_states:
                r = SetUtils.union_all_fn(s, self._transition_function, symbol)
                dfa.add_transition(s, symbol, self._e_close(r))

        return dfa
