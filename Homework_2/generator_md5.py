import os
import hashlib


def generator(path):
    with open(path, 'rb') as f:
        for string in f:
            yield string


for string in generator(os.path.abspath('countries.txt')):
    print(hashlib.md5(string).hexdigest())
