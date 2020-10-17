class CFG:
    def __init__(self, variables, terminals, productions, start_symbol, is_normalized=False):
        self._variables = frozenset(variables)
        self._terminals = frozenset(terminals)
        self._productions = frozenset(productions)
        self._start_symbol = start_symbol
        self._is_normalized = is_normalized

    def __eq__(self, other):
        result = True
        result = result and self._variables == other._variables
        result = result and self._terminals == other._terminals
        result = result and self._productions == other._productions
        result = result and self._start_symbol == other._start_symbol
        return result

    def _replace_start_symbol(self):
        # Check if start symbol is on the right side of productions.
        start_symbol = self._start_symbol
        variables = self._variables
        productions = self._productions

        if len(tuple(filter(lambda p: start_symbol in p[-1], productions))) > 0:
            start_symbol = '$0'
            variables = variables.union((start_symbol,))
            productions = self._productions.union(((start_symbol, (self._start_symbol,)),))

        return CFG(
            variables=variables,
            terminals=self._terminals,
            productions=productions,
            start_symbol=start_symbol
        )

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
            # Check if start symbol is on the right side of productions.
            return self._replace_start_symbol()

    def accept(self, string):
        if self._is_normalized:
            return False
        else:
            return self.normalize().accept(string)
