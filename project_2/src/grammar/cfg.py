class CFG:
    def __init__(self, variables, terminals, productions, start_symbol):
        self._variables = frozenset(variables)
        self._terminals = frozenset(terminals)
        self._productions = frozenset(productions)
        self._start_symbol = start_symbol
