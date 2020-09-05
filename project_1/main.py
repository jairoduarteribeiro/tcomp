from os.path import join, dirname, realpath
from time import time
from src.automaton.dawg import DAWG
from src.utils.file_utils import FileUtils


if __name__ == '__main__':
    path = join(dirname(realpath(__file__)), 'waltz.txt')
    data = FileUtils.prepare_data(path)

    # Build DAWG from dataset.
    current_time = time()
    dawg = DAWG(data)
    print(f'Build DAWG (NFA): {time() - current_time} seconds.')

    # Convert DAWG to DFA.
    current_time = time()
    dfa = dawg.convert_to_dfa()
    print(f'Convert DAWG to DFA: {time() - current_time} seconds.')
