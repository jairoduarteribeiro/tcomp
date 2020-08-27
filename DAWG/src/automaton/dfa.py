class DFA():
    def __init__(self, states, alphabet, start_state, final_states,
                 transition_table=dict()):
        self._states = frozenset(states)
        self._alphabet = frozenset(alphabet)
        self._start_state = start_state
        self._final_states = frozenset(final_states)
        self._transition_table = transition_table

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

    def add_transition(self, state_before, symbol, state_after):
        self._transition_table[(state_before, symbol)] = state_after

    def accept(self, string):
        return (
            self._ext_transition_function(self._start_state, string)
            in self._final_states
        )
