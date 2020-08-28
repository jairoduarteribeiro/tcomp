import unittest
from os.path import join, dirname, realpath
from src.utils.file_utils import FileUtils


class FileUtilsTestCase(unittest.TestCase):
    def test_prepare_data(self):
        path = join(dirname(realpath(__file__)), 'sample.txt')
        self.assertEqual(FileUtils.prepare_data(path), {'aba +', 'baa +', 'b +', 'a',
                                                        'bab', 'aaa'})
