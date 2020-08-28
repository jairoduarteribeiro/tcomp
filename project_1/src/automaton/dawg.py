from src.automaton.nfa import NFA
from src.utils.set_utils import SetUtils


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

    @staticmethod
    def _p(x):
        if isinstance(x, frozenset):
            return SetUtils.union_all_fn(x, DAWG._p)
        else:
            return frozenset([x[0:i] for i in range(len(x) + 1)])

    @staticmethod
    def _left_quotients(w, x):
        result = filter(lambda el: el[0:len(w)] == w, x)
        result = map(lambda el: el[len(w):], result)
        return frozenset(result)

    def build(self, data):
        self._sample = self._build_sample(data)
        print(self._sample)
