from dfa import DFA
from functools import reduce


class NFA(DFA):
    def __init__(self, states, alphabet, start_state, final_states):
        super().__init__(states, alphabet, start_state, final_states)

    def _eclose(self, st):
        if isinstance(st, set):

            def reduce_fn(acc, curr):
                return acc.union(self._eclose(curr))

            return reduce(reduce_fn, st, set(),)
        else:
            try:
                epsilon_transitions = self._transition_function(st, "")
                return {st}.union(self._eclose(epsilon_transitions))
            except KeyError:
                return {st}


if __name__ == "__main__":

    class A(NFA):
        def __init__(self):
            super().__init__({0, 1, 2, 3}, {"a", "b"}, 0, {2})
            self._transition_table[(0, "0")] = 1
            self._transition_table[(1, "")] = 3
            self._transition_table[(0, "")] = 2
            self._transition_table[(2, "")] = 1

        def test(self):
            print(self._eclose({0, 1}))

    a = A()
    a.test()
