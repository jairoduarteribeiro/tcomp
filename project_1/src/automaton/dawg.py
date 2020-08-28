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

    @staticmethod
    def _v(x):
        v = map(lambda w: (w, DAWG._left_quotients(w, x)), DAWG._p(x))
        return {w: x for w, x in v}

    @staticmethod
    def _l(v):
        words = sorted(v.keys(), key=lambda w: len(w))
        t = words[-1]
        labels = dict()

        for word in words:
            if word:
                if v[word] != frozenset():
                    labels[(v[word[:-1]], v[word])] = frozenset([word[-1]])

                if '' in v[word]:
                    labels[(v[word[:-1]], v[t])] = frozenset([word[-1]])

        return labels

    def build(self, data):
        self._sample = self._build_sample(data)
        print(self._sample)
