class FileUtils:
    @staticmethod
    def prepare_data(path):
        f = open(path, 'r')
        data = f.readlines()[0:-1]
        f.close()
        data = map(lambda d: d.strip().replace('\t', ' '), data)
        return set(data)

    @staticmethod
    def read_csv(path):
        f = open(path, 'r')
        data = f.readlines()[1:]
        f.close()
        data = map(lambda line: line.strip().split(','), data)
        data = map(lambda line: (line[0] == 'amyloid', line[1]), data)
        result = {
            True: set(),
            False: set()
        }

        for value, word in data:
            result[value].add(word)

        return result
