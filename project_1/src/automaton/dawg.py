from src.automaton.nfa import NFA


class DAWG(NFA):
    def __init__(self, data=None):
        super().__init__(set(), set(), None, set())
        self._sample = dict()

        if data:
            self.build(data)

    @staticmethod
    def _build_sample(data):
        positive = frozenset(filter(lambda l: l.split(' ')[-1] == '+', data))
        positive = frozenset(map(lambda p: p.split(' ')[0], positive))
        negative = frozenset(filter(lambda l: l.split(' ')[-1] != '+', data))
        negative = frozenset(map(lambda p: p.split(' ')[0], negative))
        return {'+': positive, '-': negative}

    def build(self, data):
        self._sample = self._build_sample(data)
        print(self._sample)
