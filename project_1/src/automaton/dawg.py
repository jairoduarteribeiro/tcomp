from src.automaton.nfa import NFA
from src.utils.set_utils import SetUtils
from functools import reduce


class DAWG(NFA):
    def __init__(self, data=None):
        super().__init__(set(), set(), None, set())

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
    def _v_a_l(x):
        model = map(lambda w: (w, DAWG._left_quotients(w, x)), DAWG._p(x))
        model = {w: x for w, x in model}

        words = sorted(model.keys(), key=lambda w: len(w))
        t = words[-1]
        labels = dict()

        for word in words:
            if word:
                if model[word] != frozenset():
                    labels[(model[word[:-1]], model[word])] = frozenset([word[-1]])

                if '' in model[word]:
                    labels[(model[word[:-1]], model[t])] = frozenset([word[-1]])

        def choose(op):
            if op == 'v':
                return frozenset(model.values())
            elif op == 'a':
                return frozenset(labels.keys())
            else:
                return labels

        return choose

    @staticmethod
    def _potency(a, s, t):
        queue = [t]
        p = dict()

        while len(queue) > 0:
            u = list(filter(lambda pair: pair[-1] == queue[0], a))

            if queue[0] == t:
                for pair_t in u:
                    p[pair_t] = 1
            else:
                w = list(filter(lambda pair: pair[0] == queue[0], a))
                try:
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

    @staticmethod
    def _transition(vertex, string, labels):
        if len(string) == 1:
            u = filter(lambda pair: pair[0] == vertex, labels.keys())
            u = filter(lambda pair: string in labels[pair], u)
            return frozenset(map(lambda pair: pair[-1], u))
        else:
            w = string[0:-1]
            a = string[-1]
            return SetUtils.union_all_fn(DAWG._transition(vertex, w, labels),
                                         DAWG._transition, a, labels)

    @staticmethod
    def _build_alphabet(set_1, set_2):
        return SetUtils.union_all_fn(set_1.union(set_2),
                                     lambda word: frozenset([char for char in word]))

    @staticmethod
    def _extend(labels, potency, alphabet, s_neg, s, t):
        a = sorted(potency.items(), key=lambda pair: pair[-1], reverse=True)
        a = map(lambda pair: pair[0], a)
        new_labels = labels.copy()

        for u, v in a:
            for symbol in alphabet:
                if symbol not in new_labels[(u, v)]:
                    new_labels[(u, v)] = new_labels[(u, v)].union(frozenset([symbol]))
                    accepted = map(lambda w: t in DAWG._transition(s, w, new_labels), s_neg)

                    if reduce(lambda acc, curr: acc or curr, accepted, False):
                        new_labels[(u, v)] = new_labels[(u, v)].difference(frozenset([symbol]))

        return new_labels

    def build(self, data):
        sample = DAWG._build_sample(data)
        v_a_l = DAWG._v_a_l(sample['+'])

        self._states = v_a_l('v')
        self._alphabet = DAWG._build_alphabet(sample['+'], sample['-'])
        self._start_state = sample['+']
        self._final_states = frozenset({''})

        potency = DAWG._potency(v_a_l('a'), self._start_state, self._final_states)
        labels = DAWG._extend(v_a_l('l'), potency, self._alphabet, sample['-'],
                              self._start_state, self._final_states)

        self._transition_table = dict()

        for pair, symbols in labels.items():
            for symbol in symbols:
                self.add_transition(pair[0], symbol, pair[1])

        print(self._transition_table)
