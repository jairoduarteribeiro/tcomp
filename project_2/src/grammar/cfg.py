class CFG:
    def __init__(self, variables, terminals, productions, start_symbol, is_normalized=False):
        self._variables = frozenset(variables)
        self._terminals = frozenset(terminals)
        self._productions = frozenset(productions)
        self._start_symbol = start_symbol
        self._is_normalized = is_normalized

    def normalize(self):
        if self._is_normalized:
            return CFG(
                variables=self._variables,
                terminals=self._terminals,
                productions=self._productions,
                start_symbol=self._start_symbol,
                is_normalized=self._is_normalized
            )
        else:
            pass

    def accept(self, string):
        return False
