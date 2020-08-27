from functools import reduce


class SetUtils:
    @staticmethod
    def union_all_fn(elements, fn, *params):
        return reduce(lambda acc, curr: acc.union(fn(curr, *params)), elements,
                      frozenset())
