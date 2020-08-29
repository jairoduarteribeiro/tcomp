from os.path import join, dirname, realpath
from src.automaton.dawg import DAWG
from src.utils.file_utils import FileUtils


if __name__ == '__main__':
    path = join(dirname(realpath(__file__)), 'waltz.txt')
    data = FileUtils.prepare_data(path)
    a = DAWG(data)
