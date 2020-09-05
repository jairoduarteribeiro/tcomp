from os.path import join, dirname, realpath
from time import time
from src.automaton.dawg import DAWG
from src.utils.file_utils import FileUtils


def process(database, fn):
    res = {
        'right': 0,
        'wrong': 0
    }

    for word in database[True]:
        r = 'right' if fn(word) else 'wrong'
        res[r] = res[r] + 1

    for word in database[False]:
        r = 'right' if not fn(word) else 'wrong'
        res[r] = res[r] + 1

    return res


if __name__ == '__main__':
    path = join(dirname(realpath(__file__)), 'waltz.txt')
    data = FileUtils.prepare_data(path)
    db = FileUtils.read_csv('waltzdb.csv')

    # Build DAWG from dataset.
    current_time = time()
    dawg = DAWG(data)
    print(f'Build DAWG (NFA): {time() - current_time} seconds.')

    # Convert DAWG to DFA.
    current_time = time()
    dfa = dawg.convert_to_dfa()
    print(f'Convert DAWG to DFA: {time() - current_time} seconds.')

    # Process database with DAWG
    current_time = time()
    result = process(db, dawg.accept)
    total = result['right'] + result['wrong']
    print(f'Process time with DAWG: {time() - current_time} seconds.')
    print(f'Result')
    print(f'- Hits: {result["right"]} ({100 * result["right"] / total}%)')
    print(f'- Misses: {result["wrong"]} ({100 * result["wrong"] / total}%)')

    # Process database with DFA
    current_time = time()
    result = process(db, dfa.accept)
    total = result['right'] + result['wrong']
    print(f'Process time with DFA: {time() - current_time} seconds.')
    print(f'Result')
    print(f'- Hits: {result["right"]} ({100 * result["right"] / total}%)')
    print(f'- Misses: {result["wrong"]} ({100 * result["wrong"] / total}%)')
