from src.automaton.nfa import NFA
from src.automaton.dfa import DFA
from src.utils.dawg_utils import DAWGUtils
from src.utils.set_utils import SetUtils
from collections import deque


class DAWG(NFA):
    def __init__(self, data=None):
        super().__init__(set(), set(), None, set(), dict())

        if data:
            self.build(data)

    def build(self, data):
        sample = DAWGUtils.build_sample(data)
        v_a_l = DAWGUtils.v_a_l(sample['+'])
        final_state = frozenset({''})

        self._states = v_a_l('v')
        self._alphabet = DAWGUtils.build_alphabet(sample['+'], sample['-'])
        self._start_state = sample['+']
        self._final_states = frozenset({final_state})

        potency = DAWGUtils.potency(v_a_l('a'), self._start_state, final_state)
        labels = DAWGUtils.extend(
            v_a_l('l'), potency, self._alphabet, sample['-'], self._start_state, final_state
        )

        self._transition_table = dict()

        for pair, symbols in labels.items():
            for symbol in symbols:
                try:
                    self._transition_table[(pair[0], symbol)].add(pair[1])
                except KeyError:
                    self._transition_table[(pair[0], symbol)] = {pair[1]}

    def convert_to_dfa(self):
        dfa_start_state = frozenset({self._start_state})
        dfa_alphabet = frozenset(self._alphabet)
        dfa_states = frozenset({dfa_start_state})
        dfa_final_states = frozenset()
        dfa_transition_table = dict()
        queue = deque({dfa_start_state})

        while queue:
            states = queue.popleft()

            for symbol in dfa_alphabet:
                new_states = SetUtils.union_all_fn(states, self._transition_function, symbol)
                dfa_transition_table[(states, symbol)] = new_states

                if new_states not in dfa_states:
                    dfa_states = dfa_states.union({new_states})
                    queue.append(new_states)

                    if new_states.intersection(self._final_states):
                        dfa_final_states = dfa_final_states.union({new_states})

        return DAWGDFA(
            states=dfa_states,
            alphabet=dfa_alphabet,
            start_state=dfa_start_state,
            final_states=dfa_final_states,
            transition_table=dfa_transition_table
        )


class DAWGDFA(DFA):
    def __init__(self, states, alphabet, start_state, final_states, transition_table):
        super().__init__(states, alphabet, start_state, final_states, transition_table)

    def _transition_function(self, state, symbol):
        try:
            return super()._transition_function(state, symbol)
        except KeyError:
            return frozenset()
