from .nfa import NFA


class DAWG(NFA):
    def __init__(self, dataset=''):
        super().__init__(set(), set(), None, set())

        if dataset:
            self.build(dataset)

    def _build_sample(self, dataset):
        f = open(dataset, 'r')
        lines = frozenset(map(lambda l: l.strip(), f.readlines()[0:-1]))
        f.close()
        positive = frozenset(filter(lambda l: l.split('\t')[-1] == '+', lines))
        positive = frozenset(map(lambda p: p.split('\t')[0], positive))
        negative = frozenset(filter(lambda l: l.split('\t')[-1] != '+', lines))
        negative = frozenset(map(lambda p: p.split('\t')[0], negative))
        return {'+': positive, '-': negative}

    def build(self, dataset):
        self._build_sample(dataset)
