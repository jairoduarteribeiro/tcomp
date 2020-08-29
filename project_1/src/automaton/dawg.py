from src.automaton.nfa import NFA
from src.utils.set_utils import SetUtils
from functools import reduce


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

    @staticmethod
    def _potency(labels, s, t):
        a = labels.keys()
        queue = [t]
        p = dict()

        while len(queue) > 0:
            u = list(filter(lambda pair: pair[-1] == queue[0], a))

            if queue[0] == t:
                for pair_t in u:
                    p[pair_t] = 1
            else:
                try:
                    w = list(filter(lambda pair: pair[0] == queue[0], a))
                    w = reduce(lambda acc, pair: acc + p[pair], w, 0)
                except KeyError:
                    queue.append(queue[0])
                    del queue[0]
                    continue
                finally:
                    for pair_v in u:
                        p[pair_v] = w

            u = filter(lambda pair: pair[0] != s, u)
            queue = queue + list(map(lambda pair: pair[0], u))
            del queue[0]

        return p

    def build(self, data):
        self._sample = self._build_sample(data)
        print(self._sample)
