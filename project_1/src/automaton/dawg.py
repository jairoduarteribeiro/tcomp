from src.automaton.nfa import NFA
from src.utils.dawg_utils import DAWGUtils


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
