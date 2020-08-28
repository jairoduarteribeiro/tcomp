class FileUtils:
    @staticmethod
    def prepare_data(path):
        f = open(path, 'r')
        data = f.readlines()[0:-1]
        f.close()
        data = map(lambda d: d.strip().replace('\t', ' '), data)
        return set(data)
