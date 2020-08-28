from .dfa import DFA
from ..utils.set_utils import SetUtils


class NFA(DFA):
    def __init__(self, states, alphabet, start_state, final_states,
                 transition_table=dict()):
        super().__init__(states, alphabet, start_state, final_states,
                         transition_table)

    def _eclose(self, st):
        if isinstance(st, frozenset):
            return SetUtils.union_all_fn(st, self._eclose)
        else:
            epsilon_transitions = self._transition_function(st, '')
            return frozenset({st}).union(self._eclose(epsilon_transitions))

    def _transition_function(self, state, symbol):
        try:
            return super()._transition_function(state, symbol)
        except KeyError:
            return frozenset()

    def _ext_transition_function(self, state, string):
        if not string:
            return self._eclose(state)
        else:
            x = string[0:-1]
            a = string[-1]

            transitions = self._ext_transition_function(state, x)
            transitions = SetUtils.union_all_fn(
                transitions, self._transition_function, a)
            return SetUtils.union_all_fn(transitions, self._eclose)

    def add_transition(self, state_before, symbol, state_after):
        super().add_transition(state_before, symbol, frozenset(state_after))

    def accept(self, string):
        result = self._ext_transition_function(self._start_state, string)
        return bool(result.intersection(self._final_states))

    def convert_to_dfa(self):
        dfa_states = SetUtils.power_set(self._states)
        dfa_start_state = self._eclose(self._start_state)
        dfa_final_states = filter(lambda s: len(
            s.intersection(self._final_states)) > 0, dfa_states)
        dfa = DFA(dfa_states, self._alphabet,
                  dfa_start_state, dfa_final_states)

        for symbol in self._alphabet:
            for s in dfa_states:
                r = SetUtils.union_all_fn(s, self._transition_function, symbol)
                dfa.add_transition(s, symbol, self._eclose(r))

        return dfa