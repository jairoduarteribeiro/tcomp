from abc import ABCMeta


class DFA(metaclass=ABCMeta):
    def __init__(self, states, alphabet, start_state, final_states):
        self._states = states
        self._alphabet = alphabet
        self._start_state = start_state
        self._final_states = final_states
        self._transition_table = dict()

    def _transition_function(self, state, symbol):
        return self._transition_table[(state, symbol)]

    def _ext_transition_function(self, state, string):
        if not string:
            return state
        else:
            x = string[0:-1]
            a = string[-1]
            return self._transition_function(
                self._ext_transition_function(state, x), a
            )

    def accept(self, string):
        return (
            self._ext_transition_function(self._start_state, string)
            in self._final_states
        )
