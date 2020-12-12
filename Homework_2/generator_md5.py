import os
import hashlib


def generator(path):
    with open(path, 'rb') as f:
        for string in f:
            yield hashlib.md5(string).hexdigest()


if __name__ == '__main__':
    for elem in generator(os.path.abspath('countries.txt')):
        print(elem)
