class DFAutomaton:
    def __init__(
        self, states, alphabet, transition_function, start_state, final_states
    ):
        self._states = states
        self._alphabet = alphabet
        self._transition_function = transition_function
        self._start_state = start_state
        self._final_states = final_states


if __name__ == "__main__":
    f = None
    s = None
    a = DFAutomaton({}, {}, f, s, {})
