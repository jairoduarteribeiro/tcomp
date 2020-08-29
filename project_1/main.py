from os.path import join, dirname, realpath
from time import time
from src.automaton.dawg import DAWG
from src.utils.file_utils import FileUtils


if __name__ == '__main__':
    path = join(dirname(realpath(__file__)), 'waltz.txt')
    data = FileUtils.prepare_data(path)
    start_time = time()
    a = DAWG(data)
    print(f'{time() - start_time} seconds.')
