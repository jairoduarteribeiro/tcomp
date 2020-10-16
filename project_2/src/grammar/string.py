from functools import reduce


class String:
    def __init__(self, symbols=tuple()):
        self._symbols = symbols

    def __repr__(self):
        return reduce(lambda acc, curr: acc + curr, self._symbols, '')

    def __eq__(self, other):
        return self.__repr__() == other
