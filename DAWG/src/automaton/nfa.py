from dfa import DFA
from functools import reduce


class NFA(DFA):
    def __init__(self, states, alphabet, start_state, final_states):
        super().__init__(states, alphabet, start_state, final_states)

    def _union_all_fn(self, elements, fn, *params):
        def reduce_fn(acc, curr):
            return acc.union(fn(curr, *params))

        return reduce(reduce_fn, elements, set())

    def _eclose(self, st):
        if isinstance(st, set):
            return self._union_all_fn(st, self._eclose)
        else:
            epsilon_transitions = self._transition_function(st, '')
            return {st}.union(self._eclose(epsilon_transitions))

    def _transition_function(self, state, symbol):
        try:
            return super()._transition_function(state, symbol)
        except KeyError:
            return set()

    def _ext_transition_function(self, state, string):
        if not string:
            return self._eclose(state)
        else:
            x = string[0:-1]
            a = string[-1]

            transitions = self._ext_transition_function(state, x)
            transitions = self._union_all_fn(
                transitions, self._transition_function, a)
            return self._union_all_fn(transitions, self._eclose)

    def accept(self, string):
        result = self._ext_transition_function(self._start_state, string)
        return bool(result.intersection(self._final_states))
